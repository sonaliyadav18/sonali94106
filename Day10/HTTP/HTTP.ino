#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "SUNBEAM";
const char* password = "1234567890";
const char* serverUrl = "http://10.154.102.60:5000/data"; 

void setup() {
  Serial.begin(115200);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi Connected");
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;

    float temperature = 28.5;
    float humidity = 65.2;

    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"temperature\": " + String(temperature) +
                      ", \"humidity\": " + String(humidity) + "}";

    int httpResponseCode = http.POST(jsonData);
    Serial.println("HTTP Response Code: " + String(httpResponseCode));

    http.end();
  }
  delay(5000);
}

