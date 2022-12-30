from mysql import connector
from mysql.connector import Error, errorcode

# create connection using MySQLConnection() class.
# connection = connector.MySQLConnection(
#     host="localhost",
#     user="root",
#     password="root21",
#     database='testing',
#     port=3306
#
# )

# create connection using connect() constructor.
# connection = connector.connect(
#     host="localhost",
#     user="root",
#     password="root21",
#     database='testing',
#     port=3306
#
# )

# Remember: You can use any-one from the above connection creation method


# wrapping all the arguments within a Python dictionary
config = {
    "host": "localhost",
    "port": 3306,
    "username": "root",
    "password": "root21",
    "database": "testing"
}

connection = connector.connect(**config)

try:
    # closing the connection
    print(connection.is_connected())

    # creating cursor object
    cursor_object = connection.cursor()

    # executing sql query in database
    cursor_object.execute('select * from student;')

    # fetch all the records
    print("Fetching all the records ...")
    print(cursor_object.fetchall())

    # closing the cursor
    cursor_object.close()

except Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something went wrong, please check your username and password correctly...")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database not exist..")

    elif err.errno == errorcode.ER_NO_SUCH_TABLE:
        print("Table name exist..")
    else:
        print(err)

finally:
    connection.close()
