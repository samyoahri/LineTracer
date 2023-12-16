#include <Servo.h>
#include <ArduinoJson.h>

const int steer = 7;
const int throttle = 8;
const int left = 3;
const int right = 2;
const int center = 4;
int c_val = 0;
int l_val = 0;
int r_val = 0;
unsigned long steer_duration;
unsigned long steer_overall_duration;
unsigned long throttle_duration;
unsigned long throttle_overall_duration;

void setup(){
  Serial.begin(115200);
  pinMode(left, INPUT);
  pinMode(right, INPUT);
  pinMode(center, INPUT);
}

void loop() {
  int c_val = digitalRead(center);
  int l_val = digitalRead(left);
  int r_val = digitalRead(right);

  if (c_val == LOW) {
    Serial.print("Center:0");
    Serial.print(",");
  }
  else {
    Serial.print("Center:1");
    Serial.print(",");
  }

  if (l_val == LOW) {
    Serial.print("left:0");
    Serial.print(",");
    }
    else {
    Serial.print("left:1");
    Serial.print(",");
    }

  if (r_val == LOW) {
    Serial.println("Right:0");
  }
  else {
    Serial.println("Right:1");
  }
  delay(10);
}