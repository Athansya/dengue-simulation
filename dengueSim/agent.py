"""
File: agent.py
Project: dengueSim
File Created: Monday, 2nd October 2023 10:22:56 am
Author: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx)
-----
Last Modified: Monday, 2nd October 2023 10:23:11 am
Modified By: Alfonso Toriz Vazquez (atoriz98@comunidad.unam.mx>)
-----
License: MIT License
-----
Description: Abstract base agent class.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
import numpy as np
import pygame


@dataclass(slots=True)
class Agent(ABC):
    """Abstract base agent class."""
    position: np.ndarray
    velocity: np.ndarray
    state: int

    def __post_init__(self):
        """_summary_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        # TODO CHANGE ERROR INFORMATION
        if self.position.shape != (2,):
            raise ValueError("Agent position must be a 1x2 array!")
        if self.velocity.shape != (2,):
            raise ValueError("Agent velocity must be a 1x2 array!")

    def move(self, max_width: int, max_height: int, random: bool=False) -> None:
        if random:
            self._randomize_velocity()
        self.position += self.velocity
        self._handle_borders(max_width, max_height)

    def update_velocity(self, new_velocity: np.ndarray) -> None:
        if new_velocity.shape != (2,):
            raise ValueError("Agent velocity must be a 1x2 array!")

        self.velocity += new_velocity

    def update_state(self, new_state: int) -> None:
        # TODO ADD TEST TO CHECK VALID STATES
        self.state = new_state

    def _handle_borders(self, max_width: int, max_height: int) -> None:
        # X-coordinate
        if self.position[0] < 0:
            self.position[0] = max_width
        elif self.position[0] > max_width:
            self.position[0] = 0
        # Y-coordinate
        if self.position[1] < 0:
            self.position[1] = max_height
        elif self.position[1] > max_height:
            self.position[1] = 0

    def draw(
        self,
        screen: pygame.Surface,
        color: str,
        radius: int|float
    ) -> None:
        pygame_vector = pygame.Vector2(self.position[0], self.position[1])
        pygame.draw.circle(screen, color, pygame_vector, radius)

    @abstractmethod
    def _randomize_velocity(self):
        """Abstract method to randomize velocity."""
        pass

    @abstractmethod
    def check_neighbors(self) -> None:
        """Abstract method for checking neighbors of agent."""
        pass

    @abstractmethod
    def apply_rules(self) -> None:
        """Abstract method for rules of agent."""
        pass