"""
File: human.py
Project: dengueSim
File Created: Sunday, 1st October 2023 7:12:15 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Sunday, 1st October 2023 7:12:58 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Human class from dengueSim.
"""
from .agent import Agent
from icecream import ic
import numpy as np
import pygame
import random


class Human(Agent):
    def __init__(self, position, velocity, state):
        super().__init__(position, velocity, state)

    def draw(self, screen: pygame.Surface, color: str, radius: int | float) -> None:
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
    human = Human(
        position=np.asarray(
            [random.uniform(0, max_position_x), random.uniform(0, max_position_y)]
        ),
        velocity=np.asarray(
            [random.uniform(0, max_position_x), random.uniform(0, max_position_y)]
        ),
        state=random.choice([0, 1, 2]),
    )

    print("Original human")
    ic(human)

    # Modifies object
    print("Updated human position")
    human.move()
    ic(human)

    print("Updated state and velocity")
    human.update_state(1)
    human.update_velocity(np.array([1, 2]))
    ic(human)

    # Checks instance
    print("Checking instance type")
    ic(type(human))
    ic(issubclass(Human, Agent))
    ic(isinstance(human, Human))
    ic(isinstance(human, Agent))


if __name__ == "__main__":
    main()