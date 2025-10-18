/*
 * Sheepthieves Robot - Main Control Program
 * 
 * This is the main Arduino sketch for controlling the robot.
 */

// Pin definitions
const int MOTOR_LEFT_FWD = 5;
const int MOTOR_LEFT_BWD = 6;
const int MOTOR_RIGHT_FWD = 9;
const int MOTOR_RIGHT_BWD = 10;

const int SENSOR_LEFT = A0;
const int SENSOR_CENTER = A1;
const int SENSOR_RIGHT = A2;

// Speed settings
const int NORMAL_SPEED = 150;
const int TURN_SPEED = 100;

// Sensor threshold
const int SENSOR_THRESHOLD = 500;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Configure motor pins as outputs
  pinMode(MOTOR_LEFT_FWD, OUTPUT);
  pinMode(MOTOR_LEFT_BWD, OUTPUT);
  pinMode(MOTOR_RIGHT_FWD, OUTPUT);
  pinMode(MOTOR_RIGHT_BWD, OUTPUT);
  
  // Configure sensor pins as inputs
  pinMode(SENSOR_LEFT, INPUT);
  pinMode(SENSOR_CENTER, INPUT);
  pinMode(SENSOR_RIGHT, INPUT);
  
  Serial.println("Sheepthieves Robot Initialized");
}

void loop() {
  // Read sensor values
  int leftSensor = analogRead(SENSOR_LEFT);
  int centerSensor = analogRead(SENSOR_CENTER);
  int rightSensor = analogRead(SENSOR_RIGHT);
  
  // Simple line following logic
  if (centerSensor > SENSOR_THRESHOLD) {
    // Line detected in center - move forward
    moveForward();
  } else if (leftSensor > SENSOR_THRESHOLD) {
    // Line detected on left - turn left
    turnLeft();
  } else if (rightSensor > SENSOR_THRESHOLD) {
    // Line detected on right - turn right
    turnRight();
  } else {
    // No line detected - stop
    stopMotors();
  }
  
  delay(10);
}

void moveForward() {
  analogWrite(MOTOR_LEFT_FWD, NORMAL_SPEED);
  analogWrite(MOTOR_LEFT_BWD, 0);
  analogWrite(MOTOR_RIGHT_FWD, NORMAL_SPEED);
  analogWrite(MOTOR_RIGHT_BWD, 0);
}

void turnLeft() {
  analogWrite(MOTOR_LEFT_FWD, TURN_SPEED);
  analogWrite(MOTOR_LEFT_BWD, 0);
  analogWrite(MOTOR_RIGHT_FWD, 0);
  analogWrite(MOTOR_RIGHT_BWD, 0);
}

void turnRight() {
  analogWrite(MOTOR_LEFT_FWD, 0);
  analogWrite(MOTOR_LEFT_BWD, 0);
  analogWrite(MOTOR_RIGHT_FWD, TURN_SPEED);
  analogWrite(MOTOR_RIGHT_BWD, 0);
}

void stopMotors() {
  analogWrite(MOTOR_LEFT_FWD, 0);
  analogWrite(MOTOR_LEFT_BWD, 0);
  analogWrite(MOTOR_RIGHT_FWD, 0);
  analogWrite(MOTOR_RIGHT_BWD, 0);
}
