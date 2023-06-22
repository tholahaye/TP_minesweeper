from abc import ABC


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


class TileMine(Tile):
    pass


class TileHint(Tile):
    def __init__(self, grid, x, y):
        super().__init__(self, grid, x, y)
        self.hint = 0
