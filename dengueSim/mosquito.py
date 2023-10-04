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
from dataclasses import dataclass
from icecream import ic
import numpy as np
import pygame
import random


@dataclass
class Mosquito(Agent):
    # Bite radius
    bite_radius: float = 1
    # Probability of infection
    transmission_probability: float = 0.3
    
    # Susceptible birth rate
    upsilon: float = 36.5
    # Infection rate per host
    var_theta: float = 73
    # Magnitude of sinusoidal fluctuations
    eta: float = 0  # or 0.35
    # Ratio of likelihood of transmission from hosts with
    # secondary and hosts primary infection to vectors
    var_phi: float = 0  # or 12
    # Phase
    phi: float = 0

    # TODO VECTORIZE CODE IN THE FUTURE, PROBABLY BY ADDING A POPULATION CLASS OR SOME
    # WAY OF STORING EVERY CHARACTERISTIC AS A NUMPY ARRAY. DONT FORGET TO ADD
    # SETTERS AND GETTERS FOR MAKING CHANGES TO THE NUMPY ARRAYS. 
    def _bite_human(self, human: Agent) -> None:
        # Check if mosquito is close to human
        if self.state == 1 and np.linalg.norm(self.position - human.position) < self.bite_radius:
            human.state = 1 if random.random() <= self.transmission_probability else 0

    def _bite_human_vect(self, human_population: list[Agent]) -> None:
        human_positions = np.array([human.position for human in human_population])
        # Calculate the Euclidean distance between the mosquito and all humans
        distances = np.linalg.norm(self.position - human_positions, axis=1)
        # Check if the mosquito is close to any human
        close_to_human = distances < self.bite_radius
        # Get the indices of the close humans
        close_human_indices = np.where(close_to_human)[0]
        # If there are close humans, update their state
        if close_human_indices.size > 0:
            # Infection probability
            infection_probabilities = np.random.random(size=close_human_indices.shape[0])
            # Update the state of the close humans based on the infection probability
            for i, index in enumerate(close_human_indices):
                human_population[index].state = 1 if infection_probabilities[i] <= self.transmission_probability else 0
        
    def apply_rules(self, human_population: list[Agent]) -> None:
        self._bite_human_vect(human_population)
        # for human in human_population:
            # self._bite_human(human)

    def check_neighbors(self, neighbors: list[Agent]) -> None:
        pass

    def _randomize_velocity(self) -> None:
        self.velocity = np.array([random.uniform(-50, 50), random.uniform(-50, 50)])


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
    mosquito.move(max_height=500, max_width=500)
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
