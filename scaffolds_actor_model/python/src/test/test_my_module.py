import pytest
from my_module import GameOfLife

def test_game_init():
    game = GameOfLife(size=10)
    assert game is not None

def test_game_colours():
    size = 10
    game = GameOfLife(size)
    for i in range(size):
        for j in range(size):
            assert game.get_status(i, j) in [0, 1]

def test_game_random_init():
    size = 100
    game1 = GameOfLife(size)
    game2 = GameOfLife(size)
    for i in range(size):
        for j in range(size):
            if game1.get_status(i, j) != game2.get_status(i, j):
                return
    assert False

def test_game_neighbours():
    size = 100
    game = GameOfLife(size)
    for i in range(size):
        for j in range(size):
            n_neighbours = len(game.get_neighbours(i, j))
            if i in [0, size-1] and j in [0, size-1]:
                assert n_neighbours == 3
            elif i in [0, size-1] or j in [0, size-1]:
                assert n_neighbours == 5
            else:
                assert n_neighbours == 8

def test_neighbours():
    size = 100
    game = GameOfLife(size)
    assert (game.get_status(1, 1) + game.get_status(1, 2) + game.get_status(1, 3)
            + game.get_status(2, 1) + game.get_status(2, 3)
            + game.get_status(3, 1) + game.get_status(3, 2) + game.get_status(3, 3)) == sum(game.get_neighbours(2, 2))
    assert (game.get_status(0, 1) + game.get_status(1, 1) + game.get_status(1, 0)) == sum(game.get_neighbours(0, 0))

def test_set_status():
    size = 100
    game = GameOfLife(size)
    status_2_2 = game.get_status(2, 2)
    game.set_status(i=1, j=1, val=0)
    game.set_status(i=0, j=0, val=1)
    assert game.get_status(2, 2) == status_2_2
    assert game.get_status(1, 1) == 0
    assert game.get_status(0, 0) == 1
    game.set_status(2, 2, 1 - status_2_2)
    assert game.get_status(2, 2) != status_2_2

def test_rule_stay_alive():
    size = 100
    game = GameOfLife(size)
    for i in range(size):
        for j in range(size):
            game.set_status(i, j, 0)
    
    game.set_status(1, 1, 1)
    assert not game.should_live(1, 1)
    game.set_status(0, 1, 1)
    assert not game.should_live(1, 1)
    game.set_status(1, 0, 1)
    assert game.should_live(1, 1)
    game.set_status(0, 0, 1)
    assert game.should_live(1, 1)
    game.set_status(1, 2, 1)
    assert not game.should_live(1, 1)
    assert game.should_live(0, 0)
    assert game.should_live(1, 0)
    assert not game.should_live(0, 1)

def test_rule_born():
    size = 100
    game = GameOfLife(size)
    for i in range(5):
        for j in range(5):
            game.set_status(i, j, 0)
    
    assert not game.should_live(1, 1)
    game.set_status(0, 1, 1)
    assert not game.should_live(1, 1)
    game.set_status(1, 0, 1)
    assert not game.should_live(1, 1)
    game.set_status(0, 0, 1)
    assert game.should_live(1, 1)
    game.set_status(1, 2, 1)
    assert not game.should_live(1, 1)
    game.set_status(0, 0, 0)
    game.set_status(1, 1, 1)
    assert game.should_live(0, 0)
    game.set_status(0, 1, 0)
    assert game.should_live(0, 1)
