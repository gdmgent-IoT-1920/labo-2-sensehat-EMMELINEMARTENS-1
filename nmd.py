from sense_hat import SenseHat
import time
from random import randint


sense = SenseHat()
sense.clear()
sense.set_rotation(180)

chars = ['N','M','D']

while True:
  for char in chars:
      color = (randint(0,255), randint(0,255), randint(0,255))
      sense.show_letter(char, text_colour=color)

      time.sleep(1)
      time.sleep(3)