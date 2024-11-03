import pymysql.cursors
# install this library pip install pymysql
try:
    print("Attempting to connect to the database with pymysql...")
    connection = pymysql.connect(
        host='database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com',
        user='admin',
        password='abhi-1708',
        database='abhinav',
        connect_timeout=10
    )
    
    with connection.cursor() as cursor:
        print("Connected to MySQL database using pymysql")
        cursor.execute("SHOW TABLES")
        result = cursor.fetchall()
        if result:
            print("Tables:", result)
        else:
            print("No tables found in the database.")

except pymysql.MySQLError as e:
    print("Error while connecting to MySQL:", e)

finally:
    if connection:
        connection.close()
        print("MySQL connection is closed")



# host: database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com <endpoint>

# database: abhinav <name of the database you created on RDS>

# user: admin <name of the master user>

# password: abhi-1708 <master password>

# mysql -h database-1.c1isuua0qsuk.us-east-1.rds.amazonaws.com -u admin -p db1 <command to connect to the database endpoint>