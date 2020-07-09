import mysql.connector

config = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost'
}


db = mysql.connector.connect()
cursor = db.cursor()
