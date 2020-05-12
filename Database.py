import sqlite3


db = sqlite3.connect('Registration')
rs = db.cursor()

#Create Table Name Register and Number is varchar 
#rs.execute('''create table Register(name varchar(50), email varchar(100), passwd varchar(10))''')
#db.commit()

rs.execute('''insert into Register values('Vivek', 'vivek@gmail.com', '123456')''')
rs.execute('select * from Register')
db.commit()
for i in rs:
    print(i)