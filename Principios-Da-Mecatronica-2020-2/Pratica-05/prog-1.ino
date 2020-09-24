void setup()
{
  //pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop()
{
  //digitalWrite(13, HIGH);
  //delay(1000); // Wait for 1000 millisecond(s)
  //digitalWrite(13, LOW);
  //delay(1000); // Wait for 1000 millisecond(s)
  
  digitalWrite(12, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(10, HIGH);
  
  delay(500);
  
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  digitalWrite(10, LOW);
  
  delay(500);
}
