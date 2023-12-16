#include <ArduinoJson.h>

int steer = 7;
int throttle = 8;
int left = 2;
int right = 3;
int center = 4;
int c_val = 0;
int l_val = 0;
int r_val = 0;

unsigned long steer_duration;
unsigned long steer_overall_duration;
unsigned long throttle_duration;
unsigned long throttle_overall_duration;


void setup(){
    Serial.begin(9600);
    pinMode(steer,INPUT);
    pinMode(throttle, INPUT);
    pinMode(left, INPUT);
    pinMode(right, INPUT);
    pinMode(center, INPUT);
}


void loop() {
    steer_duration = pulseIn(steer,HIGH);
    steer_overall_duration = pulseIn(steer,LOW);
    steer_overall_duration += steer_duration;

    throttle_duration = pulseIn(steer,HIGH);
    throttle_overall_duration = pulseIn(steer,LOW);
    throttle_overall_duration += throttle_duration;

    Serial.print("steer_duration : ");
    Serial.print(steer_duration);
    Serial.print("/");

    Serial.print(steer_overall_duration);
    Serial.print(" throttle_duration : ");
    Serial.print(throttle_duration);
    Serial.print("/");
    Serial.printin(throttle_overall_duration);

    if(c_val == LOW){
        Serial.printin(1);
    }
    else{
        Serial.printin(0);
    }

    if(l_val == LOW){
        Serial.printin(1);
    }
    else{
        Serial.printin(0);
    }

    if(r_val == LOW){
        Serial.printin(1);
    }
    else{
        Serial.printin(0);
    }
    delay(500);
}

