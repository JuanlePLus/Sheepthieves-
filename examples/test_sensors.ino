/*
 * Sheepthieves Robot - Sensor Test Program
 * 
 * This program tests the sensors and displays their readings
 * via serial monitor.
 */

// Pin definitions
const int SENSOR_LEFT = A0;
const int SENSOR_CENTER = A1;
const int SENSOR_RIGHT = A2;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Configure sensor pins as inputs
  pinMode(SENSOR_LEFT, INPUT);
  pinMode(SENSOR_CENTER, INPUT);
  pinMode(SENSOR_RIGHT, INPUT);
  
  Serial.println("=== Sheepthieves Sensor Test ===");
  Serial.println("Format: LEFT | CENTER | RIGHT");
  Serial.println("================================");
}

void loop() {
  // Read sensor values
  int leftValue = analogRead(SENSOR_LEFT);
  int centerValue = analogRead(SENSOR_CENTER);
  int rightValue = analogRead(SENSOR_RIGHT);
  
  // Display readings
  Serial.print(leftValue);
  Serial.print(" | ");
  Serial.print(centerValue);
  Serial.print(" | ");
  Serial.println(rightValue);
  
  // Wait before next reading
  delay(200);
}
