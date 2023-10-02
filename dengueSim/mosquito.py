'''
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
'''
from dataclasses import dataclass
import random

@dataclass(slots=True)
class Mosquito():
    position: tuple[float, float] 
    velocity: tuple[float, float] 
    state: int

    # def __post_init__(self):
        # if len(self.position) != 2:
            # raise ValueError("Mosquito position must be a tuple of length 2")
        # if len(self.velocity) != 2:
            # raise ValueError("Mosquito velocity must be a tuple of length 2")


if __name__ == "__main__":
    mosquito = Mosquito(
        position=(random.uniform(0, 10), random.uniform(0, 10)),
        velocity=(random.uniform(-1, 1), random.uniform(-1, 1))
    )