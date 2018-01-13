#You can import any modules required here
import subprocess
text = '""'

#This is name of the module - it can be anything you want
moduleName = ""

#These are the words you must say for this module to be executed
commandWords = [""]


#This is the main function which will be execute when the above command words are said
def execute(command):
    subprocess.call('espeak -s80 -vfr '+text, shell=True)
