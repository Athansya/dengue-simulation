"""
File: population.py
Project: dengueSim
File Created: Tuesday, 3rd October 2023 5:43:09 pm
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Tuesday, 3rd October 2023 5:43:11 pm
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: 
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from icecream import ic
import numpy as np
import pygame


@dataclass(slots=True)
class Population(ABC):
    size: int = 10
    max_position_x: float = 500
    max_position_y: float = 500
    max_velocity: float = 10
    states: dict[str, int] = field(
        default_factory=lambda: {"susceptible": 0, "infected": 1, "recovered": 2}
    )
    states_color_map: dict[int, str] = field(
        default_factory=lambda: {0: "blue", 1: "red", 2: "green"}
    )

    _positions_matrix: np.ndarray = field(init=False)
    _velocities_matrix: np.ndarray = field(init=False)
    _states_matrix: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        # Initialize positions, veloities and states
        self._init_positions()
        self._init_velocities()
        self._init_states()

    def _init_positions(self) -> None:
        self._positions_matrix = np.zeros(shape=(self.size, 2))

        self._positions_matrix[:, 0] = np.random.uniform(
            0, self.max_position_x, size=self.size
        )
        self._positions_matrix[:, 1] = np.random.uniform(
            0, self.max_position_y, size=self.size
        )

    def _init_velocities(self) -> None:
        self._velocities_matrix = np.random.uniform(
            -self.max_velocity, self.max_velocity, size=(self.size, 2)
        )

    def _init_states(self) -> None:
        self._states_matrix = np.random.choice(
            list(self.states.values())[:-1], size=(self.size, 1)
        )

    def _handle_borders(self) -> None:
        # Check if positions are out of bounds
        # X-coordinate
        self._positions_matrix[:, 0] = np.where(
            self._positions_matrix[:, 0] > self.max_position_x,  # Exceeded width
            0,  # Value to replace it with
            self._positions_matrix[:, 0],  # else keep the same
        )

        self._positions_matrix[:, 0] = np.where(
            self._positions_matrix[:, 0] < 0,  # Less than 0
            self.max_position_x,  # Value to replace it with
            self._positions_matrix[:, 0],  # else keep the same
        )
        # Y-coordinate
        self._positions_matrix[:, 1] = np.where(
            self._positions_matrix[:, 1] > self.max_position_y,  # Exceeded height
            0,  # Value to replace it with
            self._positions_matrix[:, 1],  # else keep the same
        )

        self._positions_matrix[:, 1] = np.where(
            self._positions_matrix[:, 1] < 0,  # Less than 0
            self.max_position_y,  # Value to replace it with
            self._positions_matrix[:, 1],  # else keep the same
        )

    def draw(self, screen: pygame.Surface, radius: int | float) -> None:
        for index, mosquito_pos in enumerate(self._positions_matrix):
            pygame_vector_pos = pygame.Vector2(mosquito_pos[0], mosquito_pos[1])
            pygame.draw.circle(
                screen,
                color=self.states_color_map[self._states_matrix[index][0]],
                center=pygame_vector_pos,
                radius=radius,
            )

    @abstractmethod
    def move(self) -> None:
        pass

    @abstractmethod
    def update_velocity(self) -> None:
        pass


@dataclass
class HumanPopulation(Population):
    # Infected rate per infected vector
    B_i: float = 0
    # Infection rate per infected host
    Beta_i: float = 0
    # Susceptible birth rate
    mu: float = 1 / 65
    # Recovery rate
    gamma: float = 365 / 7
    # Temporary cross-immunity rate
    alpha: float = 2

    # Timer that keeps track of how long each human has been infected
    time_to_recover: float = 50
    time_to_susceptible: float = 50
    _infection_timer_matrix: np.ndarray = field(init=False)
    _recover_timer_matrix: np.ndarray = field(init=False)
    

    def _init_states(self) -> None:
        # Every human is susceptible at the start
        self._states_matrix = np.zeros(shape=(self.size, 1))
        self._infection_timer_matrix = np.zeros(shape=(self.size, 1))
        self._recover_timer_matrix = np.zeros(shape=(self.size, 1))

    def move(self, random: bool = False) -> None:
        if random:
            self._init_velocities()
        self._positions_matrix += self._velocities_matrix
        self._handle_borders()

    def update_velocity(self) -> None:
        pass

    def _time_infected(self) -> None:
        infected_humans = self._states_matrix == self.states["infected"]
        if np.any(infected_humans):
            self._infection_timer_matrix[infected_humans] += 1

    def recover(self) -> None:
        self._time_infected()
        humans_ready_to_recover = self._infection_timer_matrix >= self.time_to_recover
        if np.any(humans_ready_to_recover):
            self._states_matrix[humans_ready_to_recover] = self.states["recovered"]
            self._infection_timer_matrix[humans_ready_to_recover] = 0

    def _time_recovered(self) -> None:
        infected_humans = self._states_matrix == self.states["recovered"]
        if np.any(infected_humans):
            self._recover_timer_matrix[infected_humans] += 1

    def make_susceptible(self) -> None:
        self._time_recovered()
        humans_ready_to_susceptible = self._recover_timer_matrix >= self.time_to_susceptible
        if np.any(humans_ready_to_susceptible):
            self._states_matrix[humans_ready_to_susceptible] = self.states["susceptible"]
            self._recover_timer_matrix[humans_ready_to_susceptible] = 0


@dataclass
class MosquitoPopulation(Population):
    # Moving every certain time
    moving_step: float = 10  # iterations
    # Bite radius
    bite_radius: float = 1
    # Biting probability
    bite_probability: float = 0.3
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

    def move(self, random: bool = False) -> None:
        # TODO ADD CONDITION TO MOVE MOSQUITOS EVERY CERTAIN ITERATIONS
        if random:
            self._init_velocities()
        self._positions_matrix += self._velocities_matrix
        self._handle_borders()

    def update_velocity(self) -> None:
        pass

    # TODO ADD PARALLEL SUPPORT
    def bite_humans(self, human_population: HumanPopulation) -> None:
        # Bite with certain probability
        probabilility = np.random.random()
        if probabilility <= self.bite_probability:
            # For each mosquito check if it is close to a human
            for mosquito_pos in self._positions_matrix:
                distances = np.linalg.norm(
                    human_population._positions_matrix - mosquito_pos, axis=1
                )
                close_to_human = distances < self.bite_radius
                susceptible_humans = human_population._states_matrix == self.states["susceptible"]
                susceptible_humans = susceptible_humans.reshape(len(susceptible_humans))
                # If there are close humans, update their state
                if np.any(close_to_human):
                    probabilities_array = np.random.random(size=close_to_human.shape[0]) <= self.transmission_probability
                    # Only changes humans state if they are close to the mosquito AND the transmission probability is met
                    # AND the human is susceptible
                    human_population._states_matrix[
                        close_to_human
                        & probabilities_array
                        & susceptible_humans
                    ] = self.states["infected"]


def main():
    mosquitoes = MosquitoPopulation(max_velocity=10)
    ic(mosquitoes._positions_matrix)
    ic(mosquitoes._velocities_matrix)
    mosquitoes.move()
    ic(mosquitoes._positions_matrix)
    ic(mosquitoes._states_matrix)
    pass


if __name__ == "__main__":
    main()
