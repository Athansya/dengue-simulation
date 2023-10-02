"""
File: pygame_test.py
Project: Pygame
File Created: Sunday, 1st October 2023 7:01:32 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 1st October 2023 7:02:21 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Simple pygame test from https://www.pygame.org/docs/
"""

# Example file showing a basic pygame "game loop"
import pygame


def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    
    player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")
    
        pygame.draw.circle(screen, "red", player_pos, 40)
    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player_pos.y += 300 * dt
        if keys[pygame.K_a]:
            player_pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player_pos.x += 300 * dt
    
        # flip() the display to put your work on screen
        pygame.display.flip()
    
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
    
    pygame.quit()


if __name__ == "__main__":
    main()
