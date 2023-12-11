#!/usr/bin/python3
import subprocess
import RPi.GPIO as GPIO
import time

led = 18
switch = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2);

print('Switch status = ', GPIO.input(switch))

time.sleep(20);#ola

subprocess.run(["sudo /usr/bin/fbi", "-d /dev/fb0  -T 1 -noverbose -a -t 5 /home/pi/RaspPlayVideo/blackimage.jpeg"]) 

while GPIO.input(switch) == 1:
    time.sleep(0.2);
    print('Switch status = ', GPIO.input(switch))
else:
    print('Vou tocar o filme')
    subprocess.run(["vlc", "filme.mp4"]) 
    print('o filme acabou')

for i in range(10):
    GPIO.output(led, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(led, GPIO.LOW)
    time.sleep(0.2)
    print('Switch status = ', GPIO.input(switch))

GPIO.cleanup()



#subprocess.run(["vlc", "bigbuckbunny_30sclip.mp4"]) 
