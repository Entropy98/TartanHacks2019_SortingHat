#include <SPI.h>

#include <nRF24L01.h>
#include <printf.h>
#include <RF24_config.h>
#include "RF24.h"

#include <Brain.h>

Brain brain(Serial);
RF24 myRadio(7,8);

struct package{
  int id=1;
  float temp=18.3;
  char text[100] = "Text to be transmitted";  
};
byte addresses[][6] = {"2"};
typedef struct package Package;
Package data;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(1000);
  myRadio.begin();
  myRadio.setChannel(115);
  myRadio.setPALevel(RF24_PA_MAX);
  myRadio.setDataRate(RF24_1MBPS);
  myRadio.openWritingPipe(addresses[0]);
  delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
  myRadio.write(&data,sizeof(data));
  data.id=data.id+1;
  data.temp=data.temp+0.1;
  Serial.print("\npackage:");
  Serial.println(data.id);
  Serial.print(data.temp);
  Serial.print(data.text);
  //delay(1000);
  if(brain.update()){
      Serial.println(brain.readCSV());
    }
}
