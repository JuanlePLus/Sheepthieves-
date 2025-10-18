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
    def __init__(self, port=None, baudrate=9600):
        """
        Initialize the robot controller
        
        Args:
            port (str): Serial port for Arduino connection
                       Linux: /dev/ttyUSB0 or /dev/ttyACM0
                       Windows: COM3, COM4, etc.
                       macOS: /dev/cu.usbserial or /dev/cu.usbmodem
            baudrate (int): Baud rate for serial communication
        """
        # Auto-detect port if not specified
        if port is None:
            port = self._detect_port()
        
        try:
            self.serial = serial.Serial(port, baudrate, timeout=1)
            time.sleep(2)  # Wait for connection to establish
            print(f"Connected to robot on {port}")
        except serial.SerialException as e:
            print(f"Error connecting to robot: {e}")
            print("\nAvailable ports:")
            self._list_ports()
            sys.exit(1)
    
    def _detect_port(self):
        """Auto-detect the Arduino port"""
        import platform
        import os
        
        system = platform.system()
        
        # Try common ports based on OS
        if system == "Linux":
            ports = ['/dev/ttyUSB0', '/dev/ttyACM0', '/dev/ttyUSB1']
        elif system == "Windows":
            ports = [f'COM{i}' for i in range(3, 10)]
        elif system == "Darwin":  # macOS
            ports = ['/dev/cu.usbserial', '/dev/cu.usbmodem']
        else:
            ports = []
        
        for port in ports:
            if system == "Windows" or os.path.exists(port):
                try:
                    s = serial.Serial(port, 9600, timeout=1)
                    s.close()
                    print(f"Auto-detected port: {port}")
                    return port
                except (OSError, serial.SerialException):
                    continue
        
        # If no port found, return default based on OS
        if system == "Windows":
            return "COM3"
        else:
            return "/dev/ttyUSB0"
    
    def _list_ports(self):
        """List available serial ports"""
        try:
            import serial.tools.list_ports
            ports = serial.tools.list_ports.comports()
            for port in ports:
                print(f"  - {port.device}: {port.description}")
        except ImportError:
            print("  Install pyserial-tools to see available ports")
    
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
