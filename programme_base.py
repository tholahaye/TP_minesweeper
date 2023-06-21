import sys

print(sys.argv)


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


def main():
    win = False
    loss = False
    while not win and not loss:
        ask_instr()


class MineSweeper:
    def __init__(self):
        self.win = False
        self.loss = False

    def open(self, x, y):
        print(f"Ouvrir la case {x}, {y}")

    def flag(self, x, y):
        print(f"Flagger la case {x}, {y}")
