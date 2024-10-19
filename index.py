import mysql.connector
# pip install mysql-connector-python <package you need to install>
from mysql.connector import Error
connection = mysql.connector.connect(
            host='database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com',
            database='abhinav',
            user='admin',
            password='abhi-1708'
        )

cr = connection.cursor()
cr.execute("show tables")
result = cr.fetchall()
print(result)


# host: database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com <endpoint>

# database: abhinav <name of the database you created on RDS>

# user: admin <name of the master user>

# password: abhi-1708 <master password>

# mysql -h database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com -u admin -p db1 <command to connect to the database endpoint>