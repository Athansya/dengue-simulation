'''
File: vectorized_population_test.py
Project: dengueSim_test
File Created: Tuesday, 3rd October 2023 8:15:34 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Tuesday, 3rd October 2023 8:15:43 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
'''

from dengueSim import HumanPopulation, MosquitoPopulation
import pygame

WIDTH = 500
HEIGHT = 500
FPS = 60

MOSQUITO_RADIUS = 1
HUMAN_RADIUS = 5

# Host population
N = 1000
# Vector population
M = 10000


def main():
    # States dict
    states = {"susceptible": 0, "infected": 1, "recovered": 2}
    color_map = {
        states["susceptible"]: "blue",
        states["infected"]: "red",
        states["recovered"]: "green",
    }

    mosquitoes = MosquitoPopulation(
        size=M,
        max_position_x=WIDTH,
        max_position_y=HEIGHT,
        max_velocity=50,
        states=states,
        states_color_map=color_map
    )

    humans = HumanPopulation(
        size=N,
        max_position_x=WIDTH,
        max_position_y=HEIGHT,
        max_velocity=10,
        states=states,
        states_color_map=color_map
    )

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((255, 255, 255))
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Mosquito population
        mosquitoes.draw(screen, MOSQUITO_RADIUS)
        mosquitoes.move()
        mosquitoes.bite_humans(humans)

        # Human population
        humans.draw(screen, HUMAN_RADIUS)
        humans.move()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()


