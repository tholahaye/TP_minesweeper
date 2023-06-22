from abc import ABC, abstractmethod


class Grid:
    def __init__(self):
        pass


class Tile(ABC):
    def __init__(self, grid, x, y):
        self._grid = grid
        self._x = x
        self._y = y
        self.is_open = False
        self.is_flagged = False

    @abstractmethod
    def __str__(self):
        if self.is_flagged:
            return "F"
        elif not self.is_open:
            return "#"
        else:
            raise NotImplementedError


class TileMine(Tile):
    pass


class TileHint(Tile):
    def __init__(self, grid, x, y):
        super().__init__(self, grid, x, y)
        self.hint = 0
