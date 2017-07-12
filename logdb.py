#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def query_helper(query):
    '''Takes an SQL query as a parameter, executes it, and returns
    the results as a list of tuples'''
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        db.close()
        return result
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if c is not None:
            db.close()


def popart():
    """Return the top 3 most popular articles of all time"""
    all = query_helper("select totalviews.title, totalviews.views "
                       "from totalviews "
                       "limit 3")
    print("\n The Top Three Articles Are:")
    for row in all:
        print("\n \t {} -- {} views" .format(row[0], row[1]))


def popauth():
    """Return the most popular article authors of all time"""
    all = query_helper("select authors.name, pop_authors_id.totviews "
                       "from authors left join pop_authors_id "
                       "on authors.id = pop_authors_id.author "
                       "group by authors.name, pop_authors_id.totviews "
                       "order by pop_authors_id.totviews desc")
    print("\n The Most Popular Article Authors of All Time Are:")
    for row in all:
        print("\n \t {} -- {} views" .format(row[0], row[1]))


def baddays():
    """Returns days on which more than 1% of requests led to errors"""
    all = query_helper("select perc_error.date, "
                       "cast(perc_error.perc_error as numeric(36,2)) "
                       "from perc_error "
                       "where perc_error.perc_error > 1.00 "
                       "group by perc_error.date, perc_error.perc_error "
                       "order by perc_error.perc_error desc ")
    print("\n On the Following Days More Than 1% of requests led to errors:")
    for row in all:
        print("\n \t {0:%B %d, %Y} -- {1:}% Errors" .format(row[0], row[1]))

if __name__ == "__main__":
    popart()
    print("\n")
    popauth()
    print("\n")
    baddays()
    print("\n")
