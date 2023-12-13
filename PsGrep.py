#!/usr/bin/python3
import subprocess


result = subprocess.run(["ps -ef | grep raspplayvideo"], shell=True, capture_output=True, text=True)

print(result.stdout)

list = result.stdout.splitlines()

print(len(list))

for element in list:
#for element in range (0, len(list)-2):
#   print(element.find("raspplayvideo.py"))

   if element.find("raspplayvideo.py") > -1 :
     # print(list[element])
      print(element)


#result.stdout.write(" ".join(list))
