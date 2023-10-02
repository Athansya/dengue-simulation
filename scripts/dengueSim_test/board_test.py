'''
File: board_test.py
Project: dengueSim_test
File Created: Sunday, 1st October 2023 7:21:21 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 1st October 2023 7:21:24 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
'''
from dengueSim import Human, Mosquito 
import pygame
import random
from icecream import ic

WIDTH = 500
HEIGHT = 500
FPS = 10

MOSQUITO_RADIUS = 3
HUMAN_RADIUS = 10

def main():
    # States dict
    states = {"susceptible": 0, "infected": 1, "recovered": 2}
    color_map = {
        states["susceptible"]: "blue",
        states["infected"]: "red",
        states["recovered"]: "green"
    }

    # Creates agents
    mosquito_population = [
        Mosquito(
            position=(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)),
            velocity=(random.uniform(-10, 10), random.uniform(-10, 10)),
            state=random.choice(list(states.values())[:-1])  # Picks random state, except recovered
        ) for _ in range(10)
    ]

    human_population = [
        Human(
            position=(random.uniform(0, WIDTH), random.uniform(0, HEIGHT)),
            velocity=(random.uniform(-5, 5), random.uniform(-5, 5)),
            state=states["susceptible"]
        ) for _ in range(10)
    ]

    # Creates pygame window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0  # Time step

    while running:
        screen.fill((0,0,0))
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mosquitos
        for mosquito in mosquito_population:
            ic(mosquito.position)
            ic(mosquito.velocity)
            # Draw
            pygame.draw.circle(
                screen,
                color=color_map[mosquito.state],
                center=pygame.Vector2(
                    mosquito.position[0],
                    mosquito.position[1]
                ),
                radius=MOSQUITO_RADIUS
            )

            # Update position
            mosquito.position = (
                mosquito.position[0] + mosquito.velocity[0],
                mosquito.position[1] + mosquito.velocity[1]
            )
             
            
            # Update velocity
            mosquito.velocity = (
                random.uniform(-10, 10),
                random.uniform(-10, 10)
            )

        # Humans
        for human in human_population:
            ic(human.position)
            ic(human.velocity)
            # Draw
            pygame.draw.circle(
                screen,
                color=color_map[human.state],
                center=pygame.Vector2(
                    human.position[0],
                    human.position[1]
                ),
                radius=HUMAN_RADIUS
            )

            # Update position
            human.position = (
                human.position[0] + human.velocity[0],
                human.position[1] + human.velocity[1]
            )

            human.velocity = (
                random.uniform(-5, 5),
                random.uniform(-5, 5)
            )

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()