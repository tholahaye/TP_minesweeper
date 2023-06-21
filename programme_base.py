import sys


class MineSweeper:
    def __init__(self):
        self.win = False
        self.loss = False
        self.is_playing = False

    def new_game(self, taille_grille):
        self.is_playing = True

    def open(self, x, y):
        if not self.is_playing:
            raise Exception("La partie n'est pas en cours.")
        else:
            print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        if not self.is_playing:
            raise Exception("La partie n'est pas en cours.")
        else:
            print(f"Flagger la case {x}, {y}")


def ask_instr():
    stop = False
    result = None
    while not stop:
        instr = input("> ")
        split_instr = instr.split(" ")
        minesweeper = MineSweeper()
        try:
            if len(split_instr) == 2:
                x = int(split_instr[0])
                y = int(split_instr[1])
                minesweeper.open(x, y)
                stop = True
            elif len(split_instr) == 3 and split_instr[0].upper() == "F":
                x = int(split_instr[1])
                y = int(split_instr[2])
                minesweeper.flag(x, y)
                stop = True
            else:
                print("Commande invalide")
        except ValueError:
            print("Coordonées invalides")
    return result

#test
def main():
    win = False
    loss = False
    nb_colonnes = sys.argv[1]
    nb_lignes = sys.argv[2]

    taille_grille = (nb_colonnes, nb_lignes)

    while not win and not loss:
        ask_instr()
