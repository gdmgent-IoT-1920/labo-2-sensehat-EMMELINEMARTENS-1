from sense_hat import SenseHat
import time
from random import randint

s = SenseHat()
s.clear()



randomcolour = (randint(0,255), randint(0,255),randint(0,255))
textcolour = (255, 255 , 255)

while True: 
    s.show_message("Hello! We are New Media Development :)",text_colour=textcolour, back_colour=randomcolour)
time.sleep(2)

