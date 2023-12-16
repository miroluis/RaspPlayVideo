#!/usr/bin/python3
import subprocess
import re
import time
import RPi.GPIO as GPIO

switch = 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(2);

def vlc_toca():
  result = subprocess.run(["ps -ef | grep RaspPlayVideo/filme.mp4"], shell=True, capture_output=True, text=True)
  print(result.stdout)
  list = result.stdout.splitlines()

  for element in list:
    elemento_pedaco = re.split('\s', element)
    elemento_pedaco = ' '.join(elemento_pedaco).split()
    print(elemento_pedaco[1])
    if(elemento_pedaco[6] != "00:00:00"):
      #print("é para abater")
      #print(elemento_pedaco[1] + ' -> ' + elemento_pedaco[6])
      #subprocess.run(["kill " + elemento_pedaco[1]], shell=True, capture_output=True, text=True)
      #print("já abati")
      print("retorna true")
      return True
  return False

def paraVLC():
  result = subprocess.run(["ps -ef | grep RaspPlayVideo/filme.mp4"], shell=True, capture_output=True, text=True)
  list = result.stdout.splitlines()

  for element in list:
    elemento_pedaco = re.split('\s', element)
    elemento_pedaco = ' '.join(elemento_pedaco).split()
    if(elemento_pedaco[6] != "00:00:00"):
      subprocess.run(["kill " + elemento_pedaco[1]], shell=True, capture_output=True, text=True)  
      
while (vlc_toca() == True):
  print("Olha o VLC está a tocar vou esperar pelo botão")
  time.sleep(0.2);
  if(GPIO.input(switch) == 0):
    paraVLC()
    #subprocess.run(["kill " + elemento_pedaco[1]], shell=True, capture_output=True, text=True)