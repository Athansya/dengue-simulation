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


@dataclass(slots=True)
class Agent(ABC):
    position: np.ndarray
    velocity: np.ndarray
    state: int

    def __post_init__(self):
        # TODO CHANGE ERROR INFORMATION
        if self.position.shape != (2,):
            raise ValueError("Agent position must be a 1x2 array!")
        if self.velocity.shape != (2,):
            raise ValueError("Agent velocity must be a 1x2 array!")

    def move(self) -> None:
        self.position += self.velocity

    def update_velocity(self, new_velocity: np.ndarray) -> None:
        if new_velocity.shape != (2,):
            raise ValueError("Agent velocity must be a 1x2 array!")

        self.velocity += new_velocity

    def update_state(self, new_state: int) -> None:
        # TODO ADD TEST TO CHECK VALID STATES
        self.state = new_state

    @abstractmethod
    def draw(self) -> None:
        """Abstract method to draw agent. MUST be overriden!"""
        pass

    @abstractmethod
    def check_neighbors(self) -> None:
        """Abstract method for checking neighbors of agent."""
        pass

    @abstractmethod
    def apply_rules(self) -> None:
        """Abstract method for rules of agent."""
        pass

    @abstractmethod
    def _handle_borders(self) -> None:
        """Abstract method for handling borders of agent."""
        pass
