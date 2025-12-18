import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id = int(input("Enter id whose temp to be updated: "))
temperature = int(input("Enter new temperature : "))

query = f"update sensor_readings SET temperature = '{temperature}' where id = '{id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

