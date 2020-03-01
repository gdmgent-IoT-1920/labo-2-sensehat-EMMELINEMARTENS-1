# # Test mario
# from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
# import time
# from random import randint

# s = SenseHat()
# s.clear()


# o = [0,0,0]
# r = [255,0,0]
# b = [0,0,255]
# sk = [80,51,53]


# # matrix 8 op 8 
# mario = [ 
#   o , o , o , o , o , o , o, o,
#   o , o , o , r , r , o , o, o,
#   o , o , o , r , r, r , o, o,
#   o , o , o , sk,  sk, o , o, o,
#   o , o , r , r , r , r , o, o,
#   o , sk , o , r , r, o , sk, o,
#   o , o , o , b , b , o , o, o,
#   o , o , b , b , b , b , o, o,
#   ]

# mariojump = [
#   o , o , o , r , r , o , o, o,
#   o , o , o , r , r, r , o, o,
#   o , o , o , sk,  sk, o , sk, o,
#   o , r , r , r , r , r , r, o,
#   o , sk , o , b , b , o , b, o,
#   o , b , b , b , b , b , b, o,
#   o , b , o , o , o , o , o, o,
#   o , o, o , o , o , o , o, o,
#   ]

# event = s.stick.wait_for_event()


# def pushed_up(event): 
#     if event.action != ACTION_RELEASED:
#         s.set_pixels(mariojump)

# def pushed_down(event):
#     if event.action != ACTION_RELEASED:
#       s.set_pixels(mario)
      
# s.stick.direction_up = pushed_up
# s.stick.direction_down = pushed_down

# juiste Mariofunctie
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time
from random import randint

s = SenseHat()
s.clear()
s.set_rotation(180)


o = [0,0,0]
r = [255,0,0]
b = [0,0,255]
sk = [80,51,53]


# matrix 8 op 8 
mario = [ 
  o , o , o , o , o , o , o, o,
  o , o , o , r , r , o , o, o,
  o , o , o , sk , sk, r , o, o,
  o , o , o , sk,  sk, o , o, o,
  o , o , r , r , r , r , o, o,
  o , sk , o , r , r, o , sk, o,
  o , o , o , b , b , o , o, o,
  o , o , b , b , b , b , o, o,
  ]

mariojump = [
  o , o , o , r , r , o , o, o,
  o , o , o , sk , sk, r , o, o,
  o , o , o , sk,  sk, o , sk, o,
  o , o , r , r , r , r , o, o,
  o , sk , o , b , b , o , b, o,
  o , b , b , b , b , b , b, o,
  o , b , o , o , o , o , o, o,
  o , o, o , o , o , o , o, o,
  ]
while True:
  event = s.stick.wait_for_event(event.direction_up)
  if event.direction == 'up':
    s.set_pixels(mario)
    time.sleep(0.2)
    s.set_pixels(mariojump)
    
