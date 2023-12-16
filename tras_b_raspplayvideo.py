
#!/usr/bin/python3
import subprocess
import RPi.GPIO as GPIO
import time

#import vlc 

led = 35
switch = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2);

print('Switch status = ', GPIO.input(switch))

#while 1:
#   GPIO.output(led, 1);
#   time.sleep(1);
#   GPIO.output(led, 0);
#   time.sleep(1);
#GPIO.output(led, 1);




while 1:
    while GPIO.input(switch) == 1:
        time.sleep(0.2);
        print('Switch status = ', GPIO.input(switch))
    else:
        print('Vou tocar o filme')
        GPIO.output(led, 1);

        subprocess.Popen(["python3", "RaspPlayVideo/PsGrep.py"])
        result = subprocess.run(["vlc RaspPlayVideo/filme.mp4 vlc://quit"], shell=True, capture_output=True, text=True)

        print(result.stdout)

        print('o filme acabou')
        time.sleep(1);

        GPIO.output(led, 0);


GPIO.cleanup()
