from abc import ABC, abstractmethod
import random as rd


class Grid:
    def __init__(self, nb_colonnes, nb_lignes):
        self.nb_colonnes = nb_colonnes
        self.nb_lignes = nb_lignes
        self._tiles = []
        for j in range(nb_lignes):
            row = []
            for i in range(nb_colonnes):
                row.append(TileHint(self, i, j))
            self._tiles.append(row)
        self.PC_MINES = 10
        all_coord = [(i, j) for i in range(self.nb_colonnes) for j in range(self.nb_lignes)]
        nb_mines = max(round(len(all_coord) * self.PC_MINES / 100), 1)  # at least one mine
        self._mines_coord = (rd.sample(all_coord, nb_mines))
        for j in range(nb_lignes):
            for i in range(nb_colonnes):
                if (i, j) in self._mines_coord:
                    self._tiles[j][i] = TileMine(self, i, j)

    def get_tile(self, x, y):
        return self._tiles[y][x]


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
