#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11
#define LIGHT_SENSOR_PIN 13 
DHT dht(DHTPIN, DHTTYPE); 

int Isik = 0;
double isikYuzde = 0;
bool tema = true;

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  
  // LDR
  Isik = analogRead(LIGHT_SENSOR_PIN);
  isikHesap();
  temaDurum();
  
  // DHT11
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("DHT11 hatalı ölçüm");
    return;
  }
  
  
  // veri gönderme işlemleri
  Serial.print(isikYuzde); // ışık yüzde
  Serial.print("/");  
  Serial.print(h);    // nem
  Serial.print("/");
  Serial.print(t);    // sıcaklık 'C
  Serial.print("/");
  Serial.print(f);  // sıcaklık 'F
  Serial.print("/");
  Serial.println(tema);  // Tema (true-false)
  delay(500);
}

void isikHesap(){
  isikYuzde = (Isik*100)/4095;
}

void temaDurum(){
  tema = (Isik>500)? true : false;
}