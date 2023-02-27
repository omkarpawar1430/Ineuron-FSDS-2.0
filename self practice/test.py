import mysql.connector
class my_sql:

    def __init__(self, host, user,passward):
        self.host= host
        self.user = user
        self.passward= passward
    
    def get_conn(self):
            self.mydb = mysql.connector.connect(host=self.host, user=self.user, password=self.passward)
            return self.mydb
        
    def get_cursor(self):
        self.cursor = self.mydb.cursor()
        return self.cursor
    
    def database(self,db_name):
        try:
            self.db_name = db_name
            return self.cursor.execute(f"create database if not exists {self.db_name}")
        except Exception as e:
            print(e)

    def table(self,sqldata):
        try:
            self.sqldata = sqldata
            self.cursor.execute(f'use {self.db_name}') 
            self.cursor.execute(f"create table if not exists  {self.sqldata}")
        except Exception as e:
            print(e)
    
    def insert(self,data):
        try:    
            self.data=data
            self.cursor.execute(f'use ineuron')
            self.cursor.execute(self.data)
            self.mydb.commit()
        except Exception as e:
            print(e)

    def details(self, detail):
        self.detail= detail
        self.cursor.execute(self.detail)
        print(self.cursor.fetchall())

    def update(self,new_update):
        try:  
            self.new_update = new_update
            self.cursor.execute(self.new_update)
            self.mydb.commit()
        except Exception as e:
            print(e)

    def delete(self, dell):
        try:
            self.dell = dell
            self.cursor.execute(self.dell)
            self.mydb.commit()

        except Exception as e:
            print(e)

db1= my_sql("localhost", "abc", "password")
db1.get_conn()
db1.get_cursor()
db1.database("ineuron")
db1.table("tab2(rollno INT(10) ,name VARCHAR(30) ,address VARCHAR(30) ,age INT(10) )")
#db1.insert("insert into tab2 values(12345,'Mudit','Dehradun',30)")
db1.details("select * from ineuron.tab2")
db1.update("UPDATE ineuron.tab2 SET age = 50 where age = 30")
# db1.details("select * from mud.tab1")
db1.delete("delete from ineuron.tab2 where age= 50")
