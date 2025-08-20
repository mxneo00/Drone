from djitellopy import Tello
import time
import pygame
import logging

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

SPEED = 20

def initDrone(tello):
    # Error handling
    try:
        tello.connect()
        logging.info(f"Battery: {tello.get_battery()}%")
        cmd = tello.send_command_with_return("command")
        logging.info(f"Command response: {cmd}")
        tello.send_rc_control(0, 0, 0, 0)
        return True

    except Exception as e:
        logging.error(f"Failed to connect: {e}")
        return False


def main():

    pygame.init()
    screen = pygame.display.set_mode((400,300))
    pygame.display.set_caption("Drone Keyboard control")

    tello = Tello()

    if not initDrone():
        logging.error("Connection failure")
        pygame.quit()
        return
    
    # Take off
    tello.takeoff()
    time.sleep(5)

    running = True
    while running:
        fb = 0
        lr = 0
        ud = 0
        yaw = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Directional
        if keys[pygame.K_w]:
            fb = SPEED
        elif keys[pygame.K_s]:
            fb = -SPEED

        if keys[pygame.K_a]:
            lr = -SPEED
        elif keys[pygame.K_d]:
            lr = SPEED

        # Vertical
        if keys[pygame.K_UP]:
            ud = SPEED
        elif keys[pygame.K_DOWN]:
            ud = -SPEED

        # Rotation
        if keys[pygame.K_q]:
            yaw = -SPEED
        elif keys[pygame.K_e]:
            yaw = SPEED
        
        # Landing
        if keys[pygame.K_ESCAPE]:
            tello.send_rc_control(0, 0, 0, 0)
            tello.land()
            running = False

        tello.send_rc_control(lr, fb, ud, yaw)

        pygame.time.delay(50)

    pygame.quit()

    



if __name__ == "__main__":
    main()

