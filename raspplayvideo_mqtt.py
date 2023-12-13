#!/usr/bin/python3
import subprocess
import RPi.GPIO as GPIO
import time

#import vlc 
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client.connect("localhost", 1883, 60)

client.loop_forever()


led = 18
switch = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2);

print('Switch status = ', GPIO.input(switch))

while 1:
    while GPIO.input(switch) == 1:
        time.sleep(0.2);
        print('Switch status = ', GPIO.input(switch))
    else:
        print('Vou tocar o filme')

        result = subprocess.run(["vlc RaspPlayVideo/filme.mp4 vlc://quit"], shell=True, capture_output=True, text=True)

        print(result.stdout)

        print('o filme acabou')


GPIO.cleanup()



#subprocess.run(["vlc", "bigbuckbunny_30sclip.mp4"]) 
