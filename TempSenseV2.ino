
int sensorPin1 = 0;

int sensorPin2 = 1;

void setup()
  {
    Serial.begin(9600);  //Start the serial connection with the computer
                           //to view the result open the serial monitor 
    pinMode(LED_BUILTIN, OUTPUT);
  }

void loop()
  {
    digitalWrite(LED_BUILTIN, HIGH);
    //Read sensor1
    int rawvoltage1 = analogRead(sensorPin1);
    
    //Read sensor2
    int rawvoltage2 = analogRead(sensorPin1);

    //convert to celsius
    float millivolts1 = (rawvoltage1/1024.0) * 5000;
    float celsius1 = millivolts1/10;

    float millivolts2 = (rawvoltage2/1024.0) * 5000;
    float celsius2 = millivolts2/10;

    float average = ((celsius1 + celsius2) / 2);

    //Output for sensor one
    //Serial.println(celsius1 + " - " + ((celsius1 * 9)/5 + 32) + "," + // sensor 1
//                   celsius2 + " - " + ((celsius2 * 9)/5 + 32)+ " , " + // senser 2
         //          average + " - " + (average * 9)/5 + 32)); // average

    Serial.print(celsius1);
    Serial.print("-");
    Serial.print( ((celsius1 * 9)/5 + 32) );    
    Serial.print(",");
    Serial.print(celsius2);
    Serial.print("-");
    Serial.print( ((celsius2 * 9)/5 + 32) );
    Serial.print(",");
    Serial.print(average);
    Serial.print("-");
    Serial.println( (average * 9)/5 + 32) ;

    delay(500);
    digitalWrite(LED_BUILTIN, LOW); 
    delay(500);
}
