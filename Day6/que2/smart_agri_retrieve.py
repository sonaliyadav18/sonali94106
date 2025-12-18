import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri",
    use_pure = True
)

query = "select * from soil_moisture";

cursor = connection.cursor()

cursor.execute(query)

soil_moisture = cursor.fetchall()

for s in soil_moisture:
    print(s)

cursor.close()

connection.close()