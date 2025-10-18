#!/usr/bin/env python3
"""
Sheepthieves Robot - High-level Control Script

This Python script provides high-level control and monitoring
for the Sheepthieves robot via serial communication.
"""

import serial
import time
import sys

class RobotController:
    def __init__(self, port='/dev/ttyUSB0', baudrate=9600):
        """
        Initialize the robot controller
        
        Args:
            port (str): Serial port for Arduino connection
            baudrate (int): Baud rate for serial communication
        """
        try:
            self.serial = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Wait for connection to establish
            print(f"Connected to robot on {port}")
        except serial.SerialException as e:
            print(f"Error connecting to robot: {e}")
            sys.exit(1)
    
    def read_data(self):
        """Read data from the robot"""
        if self.serial.in_waiting > 0:
            try:
                line = self.serial.readline().decode('utf-8').strip()
                return line
            except UnicodeDecodeError:
                return None
        return None
    
    def send_command(self, command):
        """
        Send a command to the robot
        
        Args:
            command (str): Command to send
        """
        self.serial.write(f"{command}\n".encode('utf-8'))
        print(f"Sent command: {command}")
    
    def monitor(self, duration=60):
        """
        Monitor robot output for a specified duration
        
        Args:
            duration (int): Duration in seconds to monitor
        """
        print(f"Monitoring robot for {duration} seconds...")
        start_time = time.time()
        
        while time.time() - start_time < duration:
            data = self.read_data()
            if data:
                print(f"Robot: {data}")
            time.sleep(0.1)
    
    def close(self):
        """Close the serial connection"""
        if self.serial and self.serial.is_open:
            self.serial.close()
            print("Connection closed")

def main():
    """Main function"""
    print("=== Sheepthieves Robot Controller ===")
    
    # Initialize controller
    controller = RobotController()
    
    try:
        # Monitor the robot
        controller.monitor(duration=30)
    except KeyboardInterrupt:
        print("\nStopping robot controller...")
    finally:
        controller.close()

if __name__ == "__main__":
    main()
