#second practice of season 3
import mysql.connector
cnx = mysql.connector.connect(user ='root',
                              password = '5862',
                              host ='127.0.0.1',
                              database = 'security' )



cursor = cnx.cursor()
for i in range(2):
    username = input('your email or gmail :')
    finder1 = username.find('@')
    if finder1 == -1:
        print('username not accepted \n example username: .....@gmail.com or email.com')
        break
    endswith = username.endswith('.com')
    if endswith == False:
        print('username not accepted \n example username: .....@gmail.com or email.com')
        break
        

    password = input('enter your password : ')    

    cursor.execute('INSERT INTO user_pas VALUES (\'{}\',\'{}\')'.format(username,password))
cnx.commit()
cnx.close()
    