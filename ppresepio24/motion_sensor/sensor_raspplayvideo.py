#!/usr/bin/python3
# -*- coding: utf-8 -*-
import subprocess
import RPi.GPIO as GPIO
import time


pir_pin = 26  # Pino do sensor PIR (usando modo BCM)


GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir_pin, GPIO.IN)

time.sleep(0.2)


def motion_function():
    print("Motion Detected")
    play_movie()


def play_movie():
    try:
        print("Starting...")
        result = subprocess.run(
            ["sudo", "-u", "pi", "vlc", "--aout=alsa", "--fullscreen", "--no-osd", "/home/pi/RaspPlayVideo/filme.mp4", "vlc://quit"],
            capture_output=True,
            text=False
        )
        print(result.stdout)
        print("Movie finished")
    except Exception as e:
        print(f"Error: {e}")


try:
    while True:
        pir_state = GPIO.input(pir_pin) 
        #print(f"PIR State: {pir_state}")

        if pir_state: 
            motion_function()
            time.sleep(2)
            
        time.sleep(0.2)
except KeyboardInterrupt:
    print("Program closed")
finally:
    GPIO.cleanup()