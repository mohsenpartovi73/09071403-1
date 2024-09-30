import mysql.connector

cnx = mysql.connector.connect(user ='root',password = '5862',host ='127.0.0.1',database = 'learn' )
cursor = cnx.cursor()
query = 'select * from people'
cursor.execute(query)

for (name,gender,age) in cursor:
    print('{} is a {} and his\her age is{}'.format(name,gender,age))

#cnx.commit()
cnx.close()