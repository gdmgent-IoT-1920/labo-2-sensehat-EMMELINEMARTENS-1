from sense_hat import SenseHat
import time
from random import randint

#avatars will be symbols in this excercices
s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def smiley():
    G = green
    Y = yellow
    B = blue
    O = nothing
    smiley = [
    O, O, Y, Y, Y, Y, O, O,
    O, Y, Y, Y, Y, Y, Y, O,
    Y, G, G, Y, Y, G, G, Y,
    Y, G, G, Y, Y, G, G, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, B, Y, Y, Y, Y, B, Y,
    O, Y, B, B, B, B, Y, O,
    O, O, Y, Y, Y, Y, O, O,
    ]
    return smiley

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    plus = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return plus

def heart():
    P = pink
    O = nothing
    heart = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return heart
def christmassTree():
  g = [154,205,50] # green

  r = [randint(0,255), randint(0,255), randint(0,255)] # red
  
  w = [255, 255, 255] # white
  
  z = [0, 0, 0] # zero light
  
  xmas_tree = [
  
  z, z, z, z, w, z, z, z,
  
  z, z, z, z, g, z, z, z,
  
  z, z, z, g, r, g, z, z,
  
  z, z, g, w, g, w, g, z,
  
  z, z, z, r, g, r, z, z,
  
  z, z, w, g, w, g, w, z,
  
  z, g, r, g, g, g, r, g,
  
  z, z, z, z, g, z, z, z,
  
  ]
  return xmas_tree

images = [smiley,raspi_logo, heart, christmassTree]
count = 0

while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(1)
    count += 1

# if we do this with images
# avatars = [images file links array]
# While True:
	# for avatar in avatars
	# 	sense.load_image(avatar)
	# sleep(1)
# this function has to be an main function