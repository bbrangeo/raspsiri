#You can import any required modules here
from sense_hat import SenseHat
sense = SenseHat()

# No color
O = (0,0,0)

# Set pink color
P = (255,100,150)

# Make the pixel heart
pixel_heart = [
O, O, O, O, O, O, O, O,
O, P, P, O, O, P, P, O,
P, P, P, P, P, P, P, P,
P, P, P, P, P, P, P, P,
O, P, P, P, P, P, P, O,
O, O, P, P, P, P, O, O,
O, O, O, P, P, O, O, O,
O, O, O, O, O, O, O, O
]

#This can be anything you want
moduleName = "love"

#All of the words must be heard in order for this module to be executed
commandWords = ["love"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
    sense.clear_sense()
    sense.set_pixels(pixel_heart)
    return
