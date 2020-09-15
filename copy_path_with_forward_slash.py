import clipboard
from threading import Thread
import time
import sys

def fix_backslash():
    
    text = sys.argv[1:]
    new_text = "".join(str(elem + " ") for elem in text)
    clipboard.copy(new_text.replace("\\","/"))
    
    
def thread_run():
    Thread(target=fix_backslash).start()

thread_run()


