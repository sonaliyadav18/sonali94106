#include<WiFi.h>
#include<ArduinoMqttClient.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *host = "test.mosquitto.org";
unsigned int port = 1883;

WiFiClient wifiClient;
MqttClient subscriber(wifiClient);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  pinMode(2, OUTPUT);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

  if(!subscriber.connect(host, port)){
    while(1);
  }
  Serial.println("Subscriber is connected to broker");
  subscriber.subscribe("room/light");
  Serial.println("Subscribed to topic : room/light");
}

void loop() {
  // put your main code here, to run repeatedly:
  int len = subscriber.parseMessage();
  if(len){
    char str[len];
    for(int i = 0 ; i < len ; i++)
      str[i] = subscriber.read();

    if(strncmp(str, "ON", 2) == 0){
      digitalWrite(2, HIGH);
      Serial.println("LED is truned ON");
    }
    else if(strncmp(str, "OFF", 3) == 0){
      digitalWrite(2, LOW);
      Serial.println("LED is truned OFF");
    }
  }
}