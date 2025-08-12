from djitellopy import Tello
import time

#test

def main():
    # Create Tello object
    tello = Tello()

    # Connect to the drone
    tello.connect()
    print(f"Battery: {tello.get_battery()}%")

    # Take off
    tello.takeoff()

    # Fly forward 50 cm
    tello.move_forward(150)

    # Rotate clockwise 90 degrees
    tello.rotate_clockwise(90)

    # Hover for 2 seconds
    time.sleep(2)

    tello.rotate_clockwise(90)
    time.sleep(5)

    # Land
    tello.land()

if __name__ == "__main__":
    main()

