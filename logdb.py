
#!/usr/bin/env python
import psycopg2

DBNAME = "news"


def popart():
    """Return the top 3 most popular articles of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select totalviews.title, totalviews.views from totalviews")
    all = c.fetchall()
    print("\n The Top Three Articles Are:")
    for row in all[:3]:
        print("\n \t {} -- {} views" .format(row[0], row[1]))
    db.close()


def popauth():
    """Return the most popular article authors of all time"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select authors.name, pop_authors_id.totviews "
              "from authors left join pop_authors_id "
              "on authors.id = pop_authors_id.author "
              "group by authors.name, pop_authors_id.totviews "
              "order by pop_authors_id.totviews desc")
    all = c.fetchall()
    print("\n The Most Popular Article Authors of All Time Are:")
    for row in all[:]:
        print("\n \t {} -- {} views" .format(row[0], row[1]))
    db.close()


def baddays():
    """Returns days on which more than 1% of requests led to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("select perc_error.date, "
    	      "cast(perc_error.perc_error as numeric(36,2)) "
              "from perc_error "
              "where perc_error.perc_error > 1.00 "
              "group by perc_error.date, perc_error.perc_error "
              "order by perc_error.perc_error desc ")
    all = c.fetchall()
    print("\n On the Following Days More Than 1% of requests led to errors:")
    for row in all[:]:
        print("\n \t {} -- {}% Errors" .format(row[0], row[1]))
if __name__ == "__main__":
    popart()
    print("\n")
    popauth()
    print("\n")
    baddays()
    print("\n")
