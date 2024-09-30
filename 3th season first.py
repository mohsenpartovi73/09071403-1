
#answer of practice_season3
import mysql.connector
cnx = mysql.connector.connect(user ='root',
                              password = '5862',
                              host ='127.0.0.1',
                              database = 'info' )


cursor = cnx.cursor()
query = 'select * from information'
cursor.execute(query)
mylist = []
for (name,weight,height) in cursor:
    m = (name,weight,height) 
    mylist.append(m)

#print(mylist) 
mylist.sort(key = lambda x : (-x[:][2]))
print(mylist)



    