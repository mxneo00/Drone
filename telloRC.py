from djitellopy import Tello
import time

#def speeds(lr_speed, height_speed, fb_speed):

def main():
    # Create Tello object
    tello = Tello()

    # Connect to the drone
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    # Take off
    tello.takeoff()

    time.sleep(5)

    # KEYBOARD CONTROLS
    # WASD (Forward, left, back, right)
    # Rotate left: Q Rotate right: E
    # Higher: H  Lower: L
    # Land: x 
    
    # Adjust to use the send_rc_control command
    
    while True:
        controller = input("Enter command: ").strip().lower()

        if controller == "w":
            tello.move_forward(20)
        elif controller == "s":
            tello.move_back(20)
        elif controller == "a":
            tello.move_left(20)
        elif controller == "d":
            tello.move_right(20)
        elif controller == "q":
            tello.rotate_counter_clockwise(20)
        elif controller == "e":
            tello.rotate_clockwise(20)
        elif controller == "h":
            tello.move_up(20)
        elif controller == "l":
            tello.move_down(20)
        elif controller == "x":
            tello.land()
            break
        else:
            print("unknown control")



if __name__ == "__main__":
    main()

