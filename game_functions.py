import sys
from pygame import *

def check_events():
    for events in event.get():
        if events.type == QUIT:
            sys.exit()
