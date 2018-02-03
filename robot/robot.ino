#include <AFMotor.h>

Motor_Right motor(1);
Motor_Left motor(2);

String command = "";

void setup() {
  Serial.begin(9600); 

}

void loop() {
  // put your main code here, to run repeatedly:
  String nextCommand = "";
  char character;
  if (Serial.available()) {
    character = Serial.read();
    if(character == ' '){
      nextCommand = command;
      command = "";
    }
    else{
      command.concat(character);
    }
  }

  if(nextCommand != ""){
    if(nextCommand == "F"){
      GoForward();
    }
    else if(nextCommand == "R"){
      TurnRight();
    }
    else if(nextCommand == "L"){
      TurnLeft();
    }
  }
}

void GoForward(){
  Motor_Right.setSpeed(200);
  Motor_Left.setSpeed(200);
  Motor_Right.run(FORWARD);
  Motor_Left.run(FORWARD);
  delay(3);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

void TurnLeft(){
  Motor_Right.setSpeed(100);
  Motor_Left.setSpeed(100);
  Motor_Right.run(BACKWARD);
  Motor_Left.run(FORWARD);
  delay(3);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

void TurnRight(){
  Motor_Right.setSpeed(100);
  Motor_Left.setSpeed(100);
  Motor_Right.run(FORWARD);
  Motor_Left.run(BACKWARD);
  delay(3);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

