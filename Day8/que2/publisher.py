import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

fan = input("Enter FAN status (ON/OFF): ")
light = input("Enter LIGHT status (ON/OFF): ")

client.publish("home/fan", fan)
client.publish("home/light", light)

client.disconnect()
