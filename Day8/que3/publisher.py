import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

pulse = int(input("Enter pulse rate (bpm): "))
spo2 = int(input("Enter SpO2 level (%): "))

client.publish("health/pulse", pulse)
client.publish("health/spo2", spo2)

client.disconnect()
