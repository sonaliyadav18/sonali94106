#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

/* WiFi Credentials */
const char* ssid = "realme";
const char* password = "87654321";

/* MQTT Broker Details */
const char* mqtt_server = "172.18.3.12";
const int mqtt_port = 1883;

/* DHT Sensor Configuration */
#define DHTPIN 4
#define DHTTYPE DHT11

WiFiClient espClient;
PubSubClient client(espClient);
DHT dht(DHTPIN, DHTTYPE);

/* Connect to WiFi */
void setup_wifi() {
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println("\nWiFi connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

/* Connect to MQTT Broker */
void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP32_Publisher")) {
      Serial.println("Connected to MQTT Broker");
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" retrying...");
      delay(2000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  dht.begin();
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  client.loop();

  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor");
    return;
  }

  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C | Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  char tempString[10];
  char humString[10];

  dtostrf(temperature, 4, 2, tempString);
  dtostrf(humidity, 4, 2, humString);

  client.publish("sensor/temperature", tempString);
  client.publish("sensor/humidity", humString);

  delay(5000);
}
