#include <AFMotor.h>

AF_DCMotor Motor_Right(2);
AF_DCMotor Motor_Left(1);

String command = "";

void setup() {
  Serial.begin(9600); 

}

void writeString(String data){
  for(int i = 0; i < data.length(); ++i){
    Serial.write(data[i]);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  String nextCommand = "";
  char character;
  if (Serial.available()) {
    character = Serial.read();
    if(character == 'q'){
      nextCommand = command;
      command = "";
    }
    else{
      command.concat(character);
    }
  }

  if(nextCommand != ""){
    if(nextCommand == "F"){
      writeString("forward\n");
      GoForward();
    }
    else if(nextCommand == "R"){
      writeString("right\n");
      TurnRight();
    }
    else if(nextCommand == "L"){
      writeString("left\n");
      TurnLeft();
    }
  }
}

void GoForward(){
  Motor_Right.setSpeed(200);
  Motor_Left.setSpeed(200);
  Motor_Right.run(BACKWARD);
  Motor_Left.run(FORWARD);
  delay(500);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

void TurnLeft(){
  Motor_Right.setSpeed(200);
  Motor_Left.setSpeed(200);
  Motor_Right.run(BACKWARD);
  Motor_Left.run(BACKWARD);
  delay(500);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

void TurnRight(){
  Motor_Right.setSpeed(200);
  Motor_Left.setSpeed(200);
  Motor_Right.run(FORWARD);
  Motor_Left.run(FORWARD);
  delay(500);
  Motor_Right.run(RELEASE);
  Motor_Left.run(RELEASE);
}

