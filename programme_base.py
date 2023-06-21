import sys


class MineSweeper:
    def __init__(self):
        self.win = False
        self.loss = False
        self.is_playing = False
        self.nb_colonnes = int(sys.argv[1])
        self.nb_lignes = int(sys.argv[2])


    def new_game(self, nb_colonnes = None, nb_lignes = None):
        self.is_playing = True
        if nb_colonnes is not None:
            self.nb_colonnes = nb_colonnes
        if nb_lignes is not None:
            self.nb_lignes = nb_lignes


        print(f"La grille est de {self.nb_colonnes} colonnes et {self.nb_lignes} lignes.")


    def quit(self):
        sys.exit("Fin de jeu")

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


def ask_instr(minesweeper):
    stop = False
    result = None
    while not stop:
        instr = input("> ")
        split_instr = instr.split(" ")
        try:
            if split_instr[0].upper() == "QUIT":
                minesweeper.quit()
            elif split_instr[0].upper() == "NEWGAME":
                if len(split_instr) == 3:
                    minesweeper.new_game(int(split_instr[1]), int(split_instr[2]))
                elif len(split_instr) == 1:
                    minesweeper.new_game()
                else :
                    print("Commande invalide")
            elif len(split_instr) == 2:
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


def main():
    win = False
    loss = False
    minesweeper = MineSweeper()

    while (not win) and (not loss):
        ask_instr(minesweeper)
