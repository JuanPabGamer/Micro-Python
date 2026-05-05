# Imports go at the top
from microbit import *

# initialize the hungriness to 0
hungriness = 0

# use a loop to continue forever
while True:
    # check if the button A was pressed
    if button_a.was_pressed():
        # increase hungriness by 1 if button A was pressed and display it
        hungriness = hungriness + 1
        display.show(hungriness)
   
    # check if the button B was pressed
    if button_b.was_pressed():
        # reinitialize hungriness to 0 and display it if button B was pressed
        hungriness = 0
        display.show(hungriness)