""" Contains the functions to simulate a game-of-life generation. """

# TODO exercise 1:
# Implement the next_generation function in a TDD way.
# Base your implementation on the GameOfLifeGrid object.
# Bonus: Most tests should not fail even if GameOfLifeGrid is broken (use mock tests).
# Make sure it is the case by replacing "from objects.objects import GameOfLifeGrid" with
# "from objects.other_objects import GameOfLifeGrid" in this file before running your tests.

from typing import List, Any

from data_structures import data_structures as ds
from objects.objects import GameOfLifeGrid


def next_generation(grid: List[List[Any]]) -> List[List[ds.State]]:
    """ Return the next game-of-life generation of the grid.

    :param grid: List[List[Any]]; the grid which evolves to the next generation
        The elements are cast to bool then State, True for alive and False for dead.
    :return: List[List[State]]; the next generation of the grid
    """
    pass
