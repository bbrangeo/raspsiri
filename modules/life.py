#You can import any modules required here
from num2words import num2words
from subprocess import call

#This is name of the module - it can be anything you want
moduleName = "life"

#These are the words you must say for this module to be executed
commandWords = ["meaning","life"]

cmd_beg= 'espeak '
cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
cmd_out= '--stdout > /home/pi/Desktop/Text.wav ' # To store the voice file
text = ""

#This is the main function which will be execute when the above command words are said
def execute(command):
    print(text)
    #Replacing ' ' with '_' to identify words in the text entered
    text = text.replace(' ', '_')

    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+cmd_out+text+cmd_end], shell=True)
    print("\n")
    print("------------------The meaning of life is 42-------------------")
    print("\n")
