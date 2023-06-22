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
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)

    def __str__(self):
        if not self.is_open:
            return super().__str__()
        return "O"


class TileHint(Tile):
    def __init__(self, grid, x, y):
        super().__init__(grid, x, y)
        self.hint = 0

    def __str__(self):
        if not self.is_open:
            return super().__str__()
        if self.hint == 0:
            return " "
        return str(self.hint)
