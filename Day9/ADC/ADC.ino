void setup() {
 Serial.begin(115200);

}
void loop()
 {
int ldrValue=analogRead(34);
Serial.print("LDR Value:");
Serial.println(ldrValue);
delay(1000);
}
