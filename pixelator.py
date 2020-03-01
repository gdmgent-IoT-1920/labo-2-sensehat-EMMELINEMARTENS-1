import sense_hat
from time import sleep, time
from random import randint

sense = sense_hat.SenseHat()
sense.set_imu_config(False, False, False)
sense.set_rotation(90)


def main():
    while True:
        x = 0
        y = 0
        sense.clear()
        
        sleeptime = 0.5
        def randomColour():
          return [randint(0,255), randint(0,255), randint(0,255)]
        
        def pixelator():
            for x in range(8):
              for y in range(8):
                sense.set_pixel(x,y,randomColour())
                sleep(sleeptime)
        pixelator()
        sense.clear()
try:
    main()
    print("Programma sluiten")
finally:
    print("Opkuisen van de matrix")
    sense.clear()