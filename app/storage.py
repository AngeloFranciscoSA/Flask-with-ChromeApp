#LET'S IMPORT US THINGS!!!
#Simple pymysql, to consult in MySQL Database!
import pymysql
#catch the database settings!
import options

#Create us connection
def connect():
    conn = pymysql.connect(host=options.dbase.host, 
                           user=options.dbase.user, 
                           password=options.dbase.password, 
                           database=options.dbase.database)

    return conn

#HERE IS MAGIC WORKS!!!
class carDB():
    def __init__(self):
        self.conn = connect()

    #login function!
    def check_login(self,user,password):

        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM user_login WHERE username = %s and password = %s", [user,password])
        dc = c.fetchall()

        if len(dc) > 0:
            return dc[0]

    #create more car in database!
    def create(self,name_car,model,year,price):

        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("INSERT INTO car (name_car,model,year,price) VALUES ('"+name_car+"','"+model+"','"+year+"','"+price+"')")
        self.conn.commit()

    #consult us car!
    def consult(self,car):
        
        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM car where name_car like '%"+car+"%' or model like '%"+car+"%'")
        dc = c.fetchall()

        return dc

    #Consult to show data in edit fields
    def consult_edit(self,id_car):
        
        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("SELECT * FROM car WHERE id_car = '"+id_car+"'")
        dc = c.fetchall()

        return dc[0]

    #LET'S UPDATE US DATA!
    def update(self,id_car,name_car,model,year,price):
        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("UPDATE car set name_car='"+name_car+"', model ='"+model+"', year='"+year+"', price='"+price+"' where id_car='"+id_car+"'")
        self.conn.commit()

    #Delete some car!
    def delete(self,id_car):
        c = self.conn.cursor(pymysql.cursors.DictCursor)
        c.execute("DELETE FROM car WHERE id_car='"+id_car+"'")
        self.conn.commit()
    