import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="device_status"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    appliance = msg.topic.split("/")[1]
    status = msg.payload.decode()

    print(appliance.upper(), "status received:", status)

    query = """
    INSERT INTO appliance_status (appliance_name, status)
    VALUES (%s, %s)
    """
    cursor.execute(query, (appliance, status))
    db.commit()

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost")
client.subscribe("home/fan")
client.subscribe("home/light")

client.loop_forever()
