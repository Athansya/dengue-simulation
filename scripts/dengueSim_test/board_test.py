"""
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
"""
from dengueSim import Human, Mosquito
from icecream import ic
import numpy as np
import pygame
import random

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
        states["recovered"]: "green",
    }

    # Creates agents
    mosquito_population = [
        Mosquito(
            position=np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)]),
            velocity=np.array([random.uniform(-10, 10), random.uniform(-10, 1)]),
            state=random.choice(
                list(states.values())[:-1]
            ),  # Picks random state, except recovered
        )
        for _ in range(10)
    ]

    human_population = [
        Human(
            position=np.array([random.uniform(0, WIDTH), random.uniform(0, HEIGHT)]),
            velocity=np.array([random.uniform(-1, 1), random.uniform(-1, 1)]),
            state=states["susceptible"],
        )
        for _ in range(10)
    ]

    # Creates pygame window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0  # Time step

    while running:
        screen.fill((0, 0, 0))
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mosquitos
        for mosquito in mosquito_population:
            # Draw
            mosquito.draw(
                screen,
                color=color_map[mosquito.state],
                radius=MOSQUITO_RADIUS
            )
            # Move
            mosquito.move()

        for human in human_population:
            human.draw(
                screen,
                color=color_map[human.state],
                radius=HUMAN_RADIUS
            )
            # Move
            human.move()


        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
