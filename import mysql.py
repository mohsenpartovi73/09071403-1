import mysql.connector

#print('connecting to db')
cnx = mysql.connector.connect(user ='root',password = '5862',host ='127.0.0.1',database = 'learn2' )
#print('connected to db')
cursor = cnx.cursor()
for i in range(4):
    name = input('name :')
    gender = input('gender:')
    age = int(input('age'))
    cursor.execute('INSERT INTO people VALUES (\'{}\',\'{}\',{})'.format(name,gender,age))
cnx.commit()
cnx.close()