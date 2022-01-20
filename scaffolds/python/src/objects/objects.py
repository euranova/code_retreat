""" Contains the original set of objects for the code. """

from data_structures import data_structures as ds


class GameOfLifeGrid:
    """ A game-of-life grid with useful functions to access neighbours.

    :param grid: List[List[Any]]; the grid
        The elements are cast to bool then State, True for alive and False for dead."""
    def __init__(self, init_grid):
        self.grid = ds.Grid([[ds.State(bool(elem)) for elem in row] for row in init_grid])

    def _is_off_grid(self, coordinates):
        return not (0 <= coordinates.x < len(self.grid.cells) and
                    0 <= coordinates.y < len(self.grid.cells[0]))

    def get_state(self, coordinates):
        """ Return the state of the cell at the given coordinates or None if it is off-grid.

        :param coordinates: Coordinates; coordinates for which we want the state
        :return: State or None; the state of the cell
        """
        if self._is_off_grid(coordinates):
            return None
        return self.grid.cells[coordinates.x][coordinates.y]

    def get_neighbours(self, coordinates):
        """ Return the neighbours' states.

        :param coordinates: Coordinates; coordinate of the cell for which we need the neighours
        :return: List[State]; the (unordered) list of neighbours states
        """
        x, y = coordinates.x, coordinates.y
        neighbour_states = []
        for x_offset in [-1, 0, 1]:
            for y_offset in [-1, 0, 1]:
                if x_offset == 0 and y_offset == 0:
                    continue
                neighbour_coordinates = ds.Coordinates(x + x_offset, y + y_offset)
                neighbour_state = self.get_state(neighbour_coordinates)
                if neighbour_state is None:
                    continue
                neighbour_states.append(neighbour_state)
        return neighbour_states
