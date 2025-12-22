import paho.mqtt.client as mqtt
import mysql.connector

# Threshold values
PULSE_LIMIT = 100
SPO2_LIMIT = 95

# MySQL connection (DATABASE NAME CHANGED ✅)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="health_monitor"
)
cursor = db.cursor()

pulse_value = None
spo2_value = None

def on_message(client, userdata, msg):
    global pulse_value, spo2_value

    topic = msg.topic
    value = int(msg.payload.decode())

    if topic == "health/pulse":
        pulse_value = value
        print("Pulse Rate received:", value)
        if value > PULSE_LIMIT:
            print("⚠ ALERT to Doctor: High Pulse Rate!")

    elif topic == "health/spo2":
        spo2_value = value
        print("SpO2 Level received:", value)
        if value < SPO2_LIMIT:
            print("⚠ ALERT to Doctor: Low Oxygen Level!")

    # Store once both values are received
    if pulse_value is not None and spo2_value is not None:
        alert = "Normal"

        if pulse_value > PULSE_LIMIT and spo2_value < SPO2_LIMIT:
            alert = "High Pulse & Low SpO2"
        elif pulse_value > PULSE_LIMIT:
            alert = "High Pulse"
        elif spo2_value < SPO2_LIMIT:
            alert = "Low SpO2"

        query = """
        INSERT INTO health_monitoring (pulse, spo2, alert_message)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (pulse_value, spo2_value, alert))
        db.commit()

        pulse_value = None
        spo2_value = None

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost")
client.subscribe("health/pulse")
client.subscribe("health/spo2")

client.loop_forever()
