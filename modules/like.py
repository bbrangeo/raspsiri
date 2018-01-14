#You can import any required modules here
import pylast
from mylast import API_KEY, API_SECRET, username, password_hash
from sense_hat import SenseHat

sense = SenseHat()

# Connect to Last FM network
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)


# Get current track
track = network.get_user(username).get_now_playing()

# Love current track
track.love()

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
moduleName = "like"

#All of the words must be heard in order for this module to be executed
commandWords = ["like song"]

def execute(command):
    print track
    print command
    sense.clear()
    sense.set_pixels(pixel_heart)
    return
