#You can import any modules required here
import subprocess
text = '"Hello world"'

#This is name of the module - it can be anything you want
moduleName = "life"

#These are the words you must say for this module to be executed
commandWords = ["meaning","life"]



#This is the main function which will be execute when the above command words are said
def execute(command):
    subprocess.call('espeak '+text, shell=True)
    print("\n")
    print("------------------The meaning of life is 42-------------------")
    print("\n")
