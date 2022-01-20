""" Contains the second set of data structures, which you need to use to reimplement
the different objects. """

from __future__ import annotations

from dataclasses import dataclass
from enum import Flag


class State(Flag):
    ALIVE = True
    DEAD = False


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Cell:
    state: State
    up_neighbour: Cell
    down_neighbour: Cell
    left_neighbour: Cell
    right_neighbour: Cell



@dataclass
class Graph:
    cells: set[Cell]
