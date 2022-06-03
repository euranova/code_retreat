""" Contains the second set of objects. """

# Todo exercise 2:
# Re-implement the GameOfLifeGrid class using the other given data structure.
# You can use the tests written in test/test_gol_grid.py to make sure your implementation is good.

from typing import List, Any, Optional

from data_structures import other_data_structures as ds


class GameOfLifeGrid:
    """ A game-of-life grid with useful functions to access neighbours.

    :param grid: List[List[Any]]; the grid
        The elements are cast to bool then State, True for alive and False for dead.
    """
    def __init__(self, init_grid: List[List[Any]]):
        raise NotImplementedError  # TODO

    def get_state(self, coordinates: ds.Coordinates) -> Optional[ds.State]:
        """ Return the state of the cell at the given coordinates or None if it is off-grid.

        :param coordinates: Coordinates; coordinates for which we want the state
        :return: State or None; the state of the cell
        """
        raise NotImplementedError  # TODO

    def get_neighbours_states(self, coordinates: ds.Coordinates) -> List[ds.State]:
        """ Return the neighbours' states.

        :param coordinates: Coordinates; coordinate of the cell for which we need the neighours
        :return: List[State]; the (unordered) list of neighbours states
        """
        raise NotImplementedError  # TODO
