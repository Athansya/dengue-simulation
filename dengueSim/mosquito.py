"""
File: mosquito.py
Project: dengueSim
File Created: Sunday, 1st October 2023 7:12:04 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 1st October 2023 7:12:27 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Mosquito class from dengueSim.
"""
from .agent import Agent
from icecream import ic
import numpy as np
import pygame
import random


class Mosquito(Agent):
    def __init__(self, position, velocity, state):
        super().__init__(position, velocity, state)

    def draw(
        self,
        screen: pygame.Surface,
        color: str,
        radius: int|float
    ) -> None:
        pygame_vector = pygame.Vector2(self.position[0], self.position[1])
        pygame.draw.circle(screen, color, pygame_vector, radius)

    def apply_rules(self) -> None:
        pass

    def check_neighbors(self, neighbors: list[Agent]) -> None:
        pass

    def _handle_borders(self) -> None:
        pass


def main():
    # Valid boundaries
    max_position_x = 500
    max_position_y = 500

    # Creates object
    mosquito = Mosquito(
        position=np.asarray(
            [random.uniform(0, max_position_x), random.uniform(0, max_position_y)]
        ),
        velocity=np.asarray(
            [random.uniform(0, max_position_x), random.uniform(0, max_position_y)]
        ),
        state=random.choice([0, 1, 2]),
    )

    print("Original mosquito")
    ic(mosquito)

    # Modifies object
    print("Updated mosquito position")
    mosquito.move()
    ic(mosquito)

    print("Updated state and velocity")
    mosquito.update_state(1)
    mosquito.update_velocity(np.array([1, 2]))
    ic(mosquito)

    # Checks instance
    print("Checking instance type")
    ic(type(mosquito))
    ic(issubclass(Mosquito, Agent))
    ic(isinstance(mosquito, Mosquito))
    ic(isinstance(mosquito, Agent))


if __name__ == "__main__":
    main()
