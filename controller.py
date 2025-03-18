import pygame
# from gpiozero import Servo
from time import sleep
pygame.init()

pygame.joystick.init()

# servo = Servo(11)


# while True:
#     servo.min()
#     print(servo.value * 10)
#     sleep(1)
        
#     servo.mid()
#     print(servo.value * 10)
#     sleep(1)
#     servo.max()
#     print(servo.value * 10)
#     sleep(1)
# Check for joystick presence
if pygame.joystick.get_count() > 0:
    # Use the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Initialized Joystick : {joystick.get_name()}")
else:
    print("No joystick detected!")
    quit()

# Loop to keep the application running
try:
    while True:
        # Update the joystick events
        pygame.event.pump()
        
        left_joystick = joystick.get_axis(0)
        print(f"left joystick {left_joystick:.2f}")

        print(servo.value)
        if left_joystick < 0:
            servo.min()
        elif left_joystick > 0:
            servo.max()
        else:
            servo.mid()
        right_trigger = joystick.get_axis(4)
        print(f"right trigger {right_trigger:.2f}")
 
        left_trigger = joystick.get_axis(5)
        print(f"left trigger {left_trigger:.2f}")

        a_button = joystick.get_button(0)
        print('A button', a_button)

        pygame.time.wait(100)

except KeyboardInterrupt:
    print("Application exited.")
