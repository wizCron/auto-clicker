import pyautogui
import time
import keyboard

# Set the number of clicks per second
clicks_per_second = 10

# Set the delay between clicks in seconds
click_delay = 1 / clicks_per_second

# Set the button to press to start and stop the clicker
start_clicking = 'g'
stop_clicking = 'j'

# Set the button to press to stop the application
kill_switch = 'k'

# Flag to track whether the script should be running
run = True

# Flag to track whether the script should be clicking
clicking = False

print(f"The clicking speed is set to {clicks_per_second} clicks per second.")
print(f"Press '{start_clicking.capitalize()}'-Key to start the clicker.")
print(f"Press '{stop_clicking.capitalize()}'-Key to stop the clicker.")
print(f"Press '{kill_switch.capitalize()}'-Key to exit the clicker.")
# Continuously check for the g and j keys to be pressed
while run:
    # Check if the g key is being held down
    if keyboard.is_pressed(start_clicking):
        # Set the clicking flag to True
        clicking = True
    # Check if the j key is being held down
    elif keyboard.is_pressed(stop_clicking):
        # Set the clicking flag to False
        clicking = False
    
    # Check the clicking flag
    if clicking:
        # Click the left mouse button
        pyautogui.click()
        # Wait for the specified delay before clicking again
        time.sleep(click_delay)
    else:
        # Wait for a short period before checking for the g key again
        time.sleep(click_delay)

    # Check if the k key is pressed while no clicking active
    if keyboard.is_pressed(kill_switch) and clicking == False:
        # Set the run flag to False to stop the script
        run = False
