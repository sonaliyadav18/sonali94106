import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost")

ldr = float(input("Enter LDR intensity value: "))
lm35 = float(input("Enter temperature (LM35): "))

client.publish("sensor/ldr", ldr)
client.publish("sensor/lm35", lm35)

client.disconnect()
