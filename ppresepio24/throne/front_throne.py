
#!/usr/bin/python3
import subprocess
import RPi.GPIO as GPIO
import time
import threading 

#import vlc 

sync = 35
switch = 37

paused = False 
bootFlag = False

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sync, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.2)


def monitor_gpio():
    global paused
    global bootFlag
    while True:
        if not bootFlag:
            time.sleep(0.2)
            continue
        if GPIO.input(switch) == 0:
            print("Pressed!")
            if not paused:
                pause_vlc()
                paused = True
                sync_to_projector()   
            else:
                resume_vlc()
                paused = False
                sync_to_projector()
            time.sleep(1)  # Debouncing


def pause_vlc():
    print("Pausing VLC")
    #subprocess.run(["xdotool", "key", "space"])

def resume_vlc():
    print("Resuming VLC")
    #subprocess.run(["xdotool", "key", "space"])

    
def sync_to_projector():
    print("sync projector")
    GPIO.output(sync, 0); # Send Signal to snyc with the other projector
    time.sleep(2)
    GPIO.output(sync, 1);



gpio_thread = threading.Thread(target=monitor_gpio)
gpio_thread.daemon = True 
gpio_thread.start()

#entry point


while 1:
        
        time.sleep(5) # Delay for the other projector to be able to receive the sync signal 
        sync_to_projector()
        bootFlag = True
        
        result = subprocess.run(
            ["sudo", "-u", "pi", "vlc", "--aout=alsa", "--fullscreen", "--no-osd", "/home/pi/RaspPlayVideo/filme.mp4", "vlc://quit"],
            capture_output=True,
            text=False
        )

        print(result.stdout)
        time.sleep(0.2)

GPIO.cleanup()