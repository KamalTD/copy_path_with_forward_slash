import clipboard
from threading import Thread
import time
import sys

# while True:
#     arg = sys.argv[1]
#     print arg
def fix_backslash():
    #while True:
    text = sys.argv[1]
    clipboard.copy(text.replace("\\","/"))
    #time.sleep(0.3)

def thread_run():
    Thread(target=fix_backslash).start()

thread_run()


