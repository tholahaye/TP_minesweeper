import sys

print(sys.argv)


def ask_coord():
    x = input("Quelle colonne voulez vous ouvrir ? : ")
    y = input("Quelle ligne voulez vous ouvrir ? : ")
    return x, y


def main():
    win = False
    loss = False
    while not win and not loss:
        ask_coord()

