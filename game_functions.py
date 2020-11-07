import sys
from pygame import *

def check_keydown_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = True
    elif event.key == K_LEFT:
        ship.moving_left = True

def check_keyup_events(event, ship):
    if event.key == K_RIGHT:
        ship.moving_right = False
    elif event.key == K_LEFT:
        ship.moving_left = False

def check_events(ship):
    for events in event.get():
        if events.type == QUIT:
            sys.exit()
        elif events.type == KEYDOWN:
            check_keydown_events(events, ship)
        elif events.type == KEYUP:
            check_keyup_events(events, ship)




def update_screen(settings, screen, ship):
    screen.fill(settings.bg_color)
    ship.blitme()

    display.flip()
