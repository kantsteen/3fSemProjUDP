from gpiozero import Button
from subprocess import Popen
from signal import pause
import os

button = Button(17, bounce_time=0.3)  # GPIO pin 17 with a debounce time of 0.3 seconds
gps_process = None  # Track the GPS script process

def toggle_script():
    global gps_process
    if gps_process is None:
        print("Button pressed. Starting COASTUDP...")
        gps_process = Popen(["python3", "/home/pi/COAST/COASTUDP.py"])
    else:
        print("Button pressed again. Stopping COASTUDP...")
        gps_process.terminate()
        gps_process.wait()
        gps_process = None
        print("COASTUDP stopped and cleaned up.")

print("Ready. Press button to start/stop COASTUDP.")
button.when_pressed = toggle_script

pause()  # Keep script running
