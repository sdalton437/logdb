# logdb.py

logdb.py is a program that uses psql and python 2.7 to return results from a database named news. The news database 
represents data from a fictional newspaper, and the python code returns the top 3 articles of all time, 
the authors ranked by views, and the days where more than 1% of requests for articles led to errors. 

# Requirements

To run this program, you will need the [FSDN-Virtual-Machine]("https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip"), the database [newsdata.sql]("https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip") and python 2.7

The newsdata.sql file must be in the same directory as the ```vagrant``` directory

Run the command: ```psql -d -f newsdata.sql``` to connect to the server

Connect to the database using ```-d news``` and create the required views by entering the following commands:
```
create view pop_authors_id as 
select articles.author, sum(totalviews.views) as totviews
from articles left join totalviews
on articles.title = totalviews.title  
group by articles.author 
order by totviews desc;
```

```
create view totalviews as 
select articles.title, count(substring(log.path,10)) as views 
from articles left join log 
on articles.slug = (select substring(log.path,10)) 
group by articles.title 
order by views desc;
```

```
create view date_status as
select date(log.time), 
case 
   when log.status = '404 NOT FOUND' then 'true'
   else 'false'
   end
from log
group by log.time, log.status
order by log.status desc;
```

```
create view tottrue as 
select distinct(date_status.date), count(date_status.case) as true 
from date_status  
where date_status.case = 'true'
group by date_status.date, date_status.case 
order by date_status.date asc;
```
```
create view totfalse as 
select distinct(date_status.date), count(date_status.case) as false
from date_status  
where date_status.case = 'false'
group by date_status.date, date_status.case 
order by date_status.date asc;
```
Once you have added these views, you can run the program using ```python logdb.py``` within the file directory

