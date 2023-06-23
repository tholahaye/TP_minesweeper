import sys
import grilles_et_cases as gd


class NoneGameError(Exception):
    pass


class OutGridError(Exception):
    pass


class MineSweeper:
    def __init__(self):
        self.win = False
        self.loss = False
        self.is_playing = False
        self.nb_colonnes = int(sys.argv[1])
        self.nb_lignes = int(sys.argv[2])

    def new_game(self, nb_colonnes=None, nb_lignes=None):
        self.is_playing = True
        if nb_colonnes is not None:
            self.nb_colonnes = nb_colonnes
        if nb_lignes is not None:
            self.nb_lignes = nb_lignes
        self.grille = gd.Grid(nb_colonnes=self.nb_colonnes, nb_lignes=self.nb_lignes)
        print(f"La grille comporte {self.nb_colonnes} colonnes et {self.nb_lignes} lignes.")

    def is_win(self):
        if self.grille.remaining == 0:
            print("Bravo ! Vous avez gagné")
            self.is_playing = False

    def is_lost(self):
        if self.grille.open_mine:
            print("Vous avez perdu !")
            self.is_playing = False

    def open(self, x, y):
        if not self.is_playing:
            raise NoneGameError()
        print(f"Ouvrir la case {x}, {y}")
        if (x, y) not in self.grille.all_coord:
            raise OutGridError()

        self.grille.open(x, y)

    def flag(self, x, y):
        if not self.is_playing:
            raise NoneGameError()
        else:
            print(f"Flagger la case {x}, {y}")
            if (x, y) not in self.grille.all_coord:
                raise OutGridError()
            else:
                self.grille.toggle_flag(x, y)


def ask_instr(minesweeper):
    while True:
        if minesweeper.is_playing:
            print(str(minesweeper.grille))
        instr = input("> ")
        split_instr = instr.split(" ")
        try:
            if split_instr[0].upper() == "QUIT":
                return True
            elif split_instr[0].upper() == "NEWGAME":
                if len(split_instr) == 3:
                    minesweeper.new_game(int(split_instr[1]), int(split_instr[2]))
                elif len(split_instr) == 1:
                    minesweeper.new_game()
                else:
                    print("Commande invalide")
            elif len(split_instr) == 2:
                x = int(split_instr[0])
                y = int(split_instr[1])
                minesweeper.open(x, y)
                minesweeper.is_lost()
                minesweeper.is_win()
                return False
            elif len(split_instr) == 3 and split_instr[0].upper() == "F":
                x = int(split_instr[1])
                y = int(split_instr[2])
                minesweeper.flag(x, y)
            else:
                print("Commande invalide")
        except ValueError:
            print("Coordonées invalides")
        except NoneGameError:
            print("La partie n'est pas en cours. Veuillez démarrer une partie.")
        except gd.OpenedError:
            print("La case que vous voulez ouvrir est déjà ouverte.")
        except gd.FlaggedError:
            print("La case que vous voulez ouvrir est déjà flaggée.")
        except OutGridError:
            print("La case que vous voulez ouvrir est hors de la grille.")


def main():
    win = False
    loss = False
    should_quit = False
    minesweeper = MineSweeper()

    while (not win) and (not loss) and not should_quit:
        should_quit = ask_instr(minesweeper)
