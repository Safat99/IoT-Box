
#include <FirebaseESP8266.h>
#include <ESP8266WiFi.h>
#include <DHT.h>


#define FIREBASE_HOST "iot-box-849d9.firebaseio.com/"
#define FIREBASE_AUTH "7t7E9MM7OVDZY8AB0PT9doiKpBq3v4ajyOB8FUcF"

#define WIFI_SSID "Tenda_48DFE8"
#define WIFI_PASSWORD "zia@zayed@zunayed123"

#define DHTPIN 12 //D6
#define led 15 //D8
#define buzzer  14//D5
#define relay1  5//D1
#define relay2  4//D2
#define relay3  0//D3
#define relay4  2//D4




#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);


FirebaseData firebaseData;
FirebaseData ledData;
FirebaseJson json;
FirebaseData relay1Data, relay2Data, relay3Data, relay4Data;



void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  //dht.begin();
  pinMode(led,OUTPUT);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  pinMode(relay3, OUTPUT);
  pinMode(relay4, OUTPUT);
  pinMode(buzzer, OUTPUT);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
  Serial.println();

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Serial.print("VOID Setup() finished!!!!!!!!!!!!!!!!!!");
}

void sensorUpdate(){
  float h = dht.readHumidity();
  float t = dht.readTemperature();// default vabe celsius e thake
  //read temp as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);
  // check if any reads failed and exit early (to try again)
  if (isnan(h) || isnan(t) || isnan(f)){
    Serial.println(F("Failed to read from DHT sensor!"));
    return;      
      }
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("% Temperature: "));
  Serial.print(t);
  Serial.print(F("C ,"));
  Serial.print(f);
  Serial.println(F("F "));

  if (Firebase.setFloat(firebaseData, "/IOT-BOX/humidity" , h)){
      Serial.println("Passed!");
      Serial.println("PATH: " + firebaseData.dataPath());
      Serial.println("------------------");
      Serial.println();
    }
  else{
      Serial.println("FAILED");
      Serial.println("REASON: " + firebaseData.errorReason());
      Serial.println("-------------------------");
      Serial.println();
    }

  if (Firebase.setFloat(firebaseData, "/IOT-BOX/temperature" , t)){
      Serial.println("Passed!");
      Serial.println("PATH: " + firebaseData.dataPath());
      Serial.println("------------------");
      Serial.println();
    }
  else{
      Serial.println("FAILED");
      Serial.println("REASON: " + firebaseData.errorReason());
      Serial.println("-------------------------");
      Serial.println();
    }
 }

void loop() {
  /*
  digitalWrite(relay1,1);
  delay(1000);
  digitalWrite(relay1,0);
  delay(1000);
  */
  sensorUpdate();

  if(Firebase.getString(ledData, "IOT-BOX/led")){
    Serial.println(ledData.stringData());
    if (ledData.stringData() == "1"){
        digitalWrite(led, 1);
    }
    else if (ledData.stringData() == "0"){
        digitalWrite(led, 0);
    }
  }

  if(Firebase.getString(relay1Data, "IOT-BOX/relay1")){
    Serial.println(relay1Data.stringData());
    if (relay1Data.stringData() == "1"){
        digitalWrite(relay1, 1);
    }
    else if (relay1Data.stringData() == "0"){
        digitalWrite(relay1, 0);
    }
  }

  if(Firebase.getString(relay2Data, "IOT-BOX/relay2")){
    Serial.println(relay2Data.stringData());
    if (relay2Data.stringData() == "1"){
        digitalWrite(relay2, 1);
    }
    else if (relay2Data.stringData() == "0"){
        digitalWrite(relay2, 0);
    }
  }

  if(Firebase.getString(relay3Data, "IOT-BOX/relay3")){
    Serial.println(relay3Data.stringData());
    if (relay3Data.stringData() == "1"){
        digitalWrite(relay3, 1);
//        for(int i=0;i<3;i++){
//          tone(buzzer,1000);  
//          delay(1000);
//          noTone(buzzer);
//          delay(1000);
//        }
    }
    else if (relay3Data.stringData() == "0"){
        digitalWrite(relay3, 0);
    }
  }
  
  if(Firebase.getString(relay4Data, "IOT-BOX/relay4")){
    Serial.println(relay4Data.stringData());
    if (relay4Data.stringData() == "1"){
        digitalWrite(relay4, 1);
//        for(int i=0;i<4;i++){
//          tone(buzzer,1000);  
//          delay(1000);
//          noTone(buzzer);
//          delay(1000);
//        }
    }
    else if (relay4Data.stringData() == "0"){
        digitalWrite(relay4, 0);
    }
  }

  delay(100);
  
}
