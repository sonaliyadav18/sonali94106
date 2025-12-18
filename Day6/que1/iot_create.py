import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

ID = int(input("Enter id : "))
Temperature = int(input("Enter Temperature : "))
Humidity = int(input("Enter humidity : "))
timestamp = int(input("Entertimestap : "))

query = f"insert into sensor_readings values({ID}, '{Temperature}', '{Humidity}', '{timestamp}');"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

