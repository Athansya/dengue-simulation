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
from dataclasses import dataclass
from icecream import ic
import numpy as np
import pygame
import random


@dataclass
class Human(Agent):
    # Infected rate per infected vector
    B_i: float = 0
    # Infection rate per infected host
    Beta_i: float = 0
    # Susceptible birth rate
    mu: float = 1/65
    # Recovery rate
    gamma: float = 365/7 
    # Temporary cross-immunity rate
    alpha: float = 2

    def apply_rules(self) -> None:
        pass

    def check_neighbors(self, neighbors: list[Agent]) -> None:
        pass

    def _randomize_velocity(self) -> None:
        self.velocity = np.array([random.uniform(-10, 10), random.uniform(-10, 10)])


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