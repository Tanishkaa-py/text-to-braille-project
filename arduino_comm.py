# arduino_comm.py

import serial
import time

def send_braille_to_arduino(pattern, port='COM3', baudrate=9600):
    try:
        arduino = serial.Serial(port, baudrate)
        time.sleep(2)  # Wait for Arduino to reset

        arduino.write((pattern + '\n').encode())  # Send pattern like "100000"
        print(f"Sent to Arduino: {pattern}")

        arduino.close()
    except Exception as e:
        print("Error sending to Arduino:", e)
