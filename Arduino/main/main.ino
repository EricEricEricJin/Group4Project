#include<Servo.h>
#define MIN_DEG 0
#define MAX_DEG 180

Servo myServo;
unsigned char* data;
int volt;
unsigned char anal_val;

void setup() {
  // put your setup code here, to run once:
  data = (unsigned char*)malloc(sizeof(unsigned char) * 2);
  Serial.begin(9600);
  pinMode(A0, INPUT);
  pinMode(13, OUTPUT);
  myServo.attach(3);
}

void loop() {
  // put your main code here, to run repeatedly:
  while(1) {
    for(int deg = MIN_DEG; deg <= MAX_DEG; deg++) {
      myServo.write(deg);
      // delay(100);
      digitalWrite(13, HIGH);
      delay(50);
      digitalWrite(13, LOW);
      delay(50);
      volt = analogRead(A0);
      anal_val = ((float)volt / 1023) * 255;
      *data = (char)deg;
      *(data + 1) = anal_val;
      Serial.write(data, 2);
    }
    for (int deg = MAX_DEG; deg >= MIN_DEG; deg --) {
      myServo.write(deg);
      // delay(100);
      digitalWrite(13, HIGH);
      delay(50);
      digitalWrite(13, LOW);
      delay(50);
      volt = analogRead(A0);
      anal_val = ((float)volt / 1023) * 255;
      *data = (char)deg;
      *(data + 1) = anal_val;
      Serial.write(data, 2);
    }
  }
}
