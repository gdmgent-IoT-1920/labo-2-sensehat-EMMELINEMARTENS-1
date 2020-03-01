import sense_hat
from time import sleep, time
from random import randint

sense = sense_hat.SenseHat()
sense.set_imu_config(False, False, False)
sense.set_rotation(180)
o = [0, 0, 0]
p = [80, 0, 80]



rectangle1 = [
  p, p, p, p ,p ,o ,o, o,
  p, o, o, o ,p ,o ,o, o,
  p, p, p, p ,p ,o ,o, o,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o
  ]

rectangle2 = [
  p, p, p, p ,p ,p ,p, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, p, p, p ,p ,p ,p, p,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o
  ]
  
rectangle3 = [
  p, p, p, p ,p ,p ,p, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, p, p, p ,p ,p ,p, p,
  o, o, o, o ,o ,o ,o, o,
  o, o, o, o ,o ,o ,o, o
  ]
  
rectangle4 = [
  p, p, p, p ,p ,p ,p, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, o, o, o ,o ,o ,o, p,
  p, p, p, p ,p ,p ,p, p
  ]

def main():
  sleeptime = 0.5
      
  while True:
         sense.set_pixels(rectangle1)
         sleep(sleeptime)
         sense.set_pixels(rectangle2)
         sleep(sleeptime)
         sense.set_pixels(rectangle3)
         sleep(sleeptime)
         sense.set_pixels(rectangle4)
         sleep(sleeptime)
         sense.clear()
         
         
try:
    main()
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()