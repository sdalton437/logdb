/* Connect with news database */

DROP DATABASE IF EXISTS news;

CREATE DATABASE news;

\c news

\i newsdata.sql

/* Create views */

/* Articles by totalviews */
create view totalviews as 
select articles.title, count(substring(log.path,10)) as views 
from articles left join log 
on articles.slug = (select substring(log.path,10)) 
group by articles.title 
order by views desc;


/* Most popular author ids */
create view pop_authors_id as 
select articles.author, sum(totalviews.views) as totviews
from articles left join totalviews
on articles.title = totalviews.title  
group by articles.author 
order by totviews desc;

/* Top authors by name */
select authors.name, pop_authors_id.totviews 
from authors left join pop_authors_id 
on authors.id = pop_authors_id.author
group by authors.name, pop_authors_id.totviews
order by pop_authors_id.totviews desc; 

/* Total trues by date */
create view tottrue as 
select date(log.time), count(log.status) as true 
from log  
where log.status = '404 NOT FOUND'
group by date(log.time);


/* Total falses by date */
create view totfalse as 
select date(log.time), count(log.status) as false
from log
group by date(log.time);

/* Display the percent error */
create view perc_error as 
select tottrue.date, (tottrue.true*100::float/totfalse.false::float) as perc_error
from tottrue left join totfalse 
on tottrue.date = totfalse.date
group by tottrue.date, tottrue.true, totfalse.false
order by tottrue.date asc;
