# logdb.py

logdb.py is a program that uses psql and python 2.7 to return results from a database named news. The news database 
represents data from a fictional newspaper, and the python code returns the top 3 articles of all time, 
the authors ranked by views, and the days where more than 1% of requests for articles led to errors. 

# Requirements

To run this program, you will need the [FSDN-Virtual-Machine]("https://d17h27t6h515a5.cloudfront.net/topher/2017/June/5948287e_fsnd-virtual-machine/fsnd-virtual-machine.zip"), the database [newsdata.sql]("https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip") and python 2.7

The newsdata.sql file must be in the same directory as the `vagrant` directory

First, bootup your virtual machine using `vagrant up` within the vagrant directory, and then login
using `vagrant ssh`

Run the command: `psql -f setup_database.sql` to setup the database

Once you have setup the database, you can run the program using ```python logdb.py``` within the file directory

