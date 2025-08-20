from djitellopy import Tello
import time


DISTANCE = 50

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
    
    while True:
        controller = input("Enter command: ").strip().lower()

        if controller == "w":
            tello.move_forward(DISTANCE)
        elif controller == "s":
            tello.move_back(DISTANCE)
        elif controller == "a":
            tello.move_left(DISTANCE)
        elif controller == "d":
            tello.move_right(DISTANCE)
        elif controller == "q":
            tello.rotate_counter_clockwise(DISTANCE)
        elif controller == "e":
            tello.rotate_clockwise(DISTANCE)
        elif controller == "h":
            tello.move_up(DISTANCE)
        elif controller == "l":
            tello.move_down(DISTANCE)
        elif controller == "x":
            tello.land()
            break
        else:
            print("unknown control")



if __name__ == "__main__":
    main()

