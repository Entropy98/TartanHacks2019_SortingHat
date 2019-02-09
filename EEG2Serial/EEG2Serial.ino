#include <Brain.h>

Brain brain(Serial);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
char* feed;
void loop() {
  // put your main code here, to run repeatedly
  if(brain.update()){
    feed=brain.readCSV();
    //Serial.println(feed);
    Serial.write(feed);
    Serial.write('\n');  
  }
}
