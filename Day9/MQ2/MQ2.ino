void setup() {
Serial.begin(115200);
}

void loop() {
  int gasValue =analogRead(35);
  Serial.print("Gas Sensor Value:");
  Serial.println(gasValue);
  delay(1000);

}
