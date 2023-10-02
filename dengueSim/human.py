'''
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
'''
from dataclasses import dataclass
import random
from pygame import Vector2

@dataclass(slots=True)
class Human():
    position: tuple[float, float] 
    velocity: tuple[float, float] 
    state: int

    # def __post_init__(self):
        # if self.position.shape != (1, 2):
            # raise ValueError("Human position must be a 1x2 array")
        # if self.velocity.shape != (1, 2):
            # raise ValueError("Human velocity must be a 1x2 array")


if __name__ == "__main__":
    mosquito = Human(
        position=(random.uniform(0, 10), random.uniform(0, 10)),
        velocity=(random.uniform(-1, 1), random.uniform(-1, 1))
    )