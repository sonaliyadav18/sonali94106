#include <WiFi.h>
#include <ArduinoMqttClient.h>
#include <DHT.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *broker = "172.18.4.146";
int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE DHT11

DHT dht(DHT_PIN, DHT_TYPE);

WiFiClient wifiClient;
MqttClient mqttClient(wifiClient);

void setup() {
  Serial.begin(115200);
  delay(1000);

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());

  Serial.print("Connecting to MQTT broker...");
  if (!mqttClient.connect(broker, port)) {
    Serial.println(" Failed!");
  } else {
    Serial.println(" Connected!");
  }
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println(" Failed to read from DHT sensor!");
    delay(2000);
    return;
  }

  if (!mqttClient.connected()) {
    Serial.println("Reconnecting to MQTT...");
    mqttClient.connect(broker, port);
  }

  mqttClient.beginMessage("reading/temp");
  mqttClient.print(temperature);
  mqttClient.endMessage();

  mqttClient.beginMessage("reading/hum");
  mqttClient.print(humidity);
  mqttClient.endMessage();

  Serial.println(" Data Published to MQTT");
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.println("------------------------");

  delay(5000);
}