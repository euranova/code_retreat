import pytest
from collections import Counter

from data_structures import data_structures as ds
from objects.objects import GameOfLifeGrid


@pytest.fixture(name="gol_grid")
def fixture_gol_grid():
    grid = [[ds.State.DEAD for _ in range(10)] for _ in range(15)]
    for x, y in [(14, 8), (13, 8), (13, 9), (12, 9)]:
        grid[x][y] = ds.State.ALIVE  # initialise the grid in an interesting state
    return GameOfLifeGrid(grid)


def test_gol_can_initialise_with_a_2d_list_containing_any_type():
    grid = [["" for _ in range(10)] for _ in range(15)]
    grid[14][9] = "this will be alive"
    GameOfLifeGrid(grid)


def test_get_state_returns_a_cell_state(gol_grid):
    assert (gol_grid.get_state(ds.Coordinates(0, 0)) is ds.State.DEAD and
            gol_grid.get_state(ds.Coordinates(14, 8)) is ds.State.ALIVE)


@pytest.mark.parametrize("coordinates", [(-1, 1), (0, 10), (2, -3), (15, 3), (16, 16), (-6, 17)])
def test_get_state_with_off_grid_coordinates_returns_none(gol_grid, coordinates: tuple):
    assert gol_grid.get_state(ds.Coordinates(*coordinates)) is None


def test_gol_initialised_with_any_type_casts_objects_into_bool_then_state():
    grid = [["" for _ in range(10)] for _ in range(15)]
    grid[14][9] = "this will be alive"
    grid = GameOfLifeGrid(grid)
    assert (grid.get_state(ds.Coordinates(14, 9)) is ds.State.ALIVE and
            grid.get_state(ds.Coordinates(13, 9)) is ds.State.DEAD)


def test_get_neighbours_states_returns_its_8_neighbours_state_when_not_at_the_border(gol_grid):
    coordinates = ds.Coordinates(13, 8)
    expected = Counter({ds.State.ALIVE: 3, ds.State.DEAD:5})
    assert Counter(gol_grid.get_neighbours_states(coordinates)) == expected


def test_get_neighbours_states_returns_its_3_neighbours_state_when_in_a_corner(gol_grid):
    coordinates = ds.Coordinates(14, 9)
    expected = Counter({ds.State.ALIVE: 3})
    assert Counter(gol_grid.get_neighbours_states(coordinates)) == expected


def test_get_neighbours_states_returns_its_5_neighbours_state_when_on_a_border(gol_grid):
    coordinates = ds.Coordinates(11, 9)
    expected = Counter({ds.State.ALIVE: 1, ds.State.DEAD: 4})
    assert Counter(gol_grid.get_neighbours_states(coordinates)) == expected
