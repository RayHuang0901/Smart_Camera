#include <Servo.h>

#define SERVO_PIN 4

Servo servo;
int currentAngle = 45;

void setup() {
  servo.attach(SERVO_PIN);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'a') {
      increaseAngle();
    } else if (command == 'b') {
      decreaseAngle();
    }
  }
}

void increaseAngle() {
  currentAngle += 1;
  if (currentAngle > 180) {
    currentAngle = 180;
  }
  servo.write(currentAngle);
}

void decreaseAngle() {
  currentAngle -= 1;
  if (currentAngle < 0) {
    currentAngle = 0;
  }
  servo.write(currentAngle);
}
