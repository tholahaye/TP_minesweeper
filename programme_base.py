import sys

print(sys.argv)

def ask_instr():
    stop = False
    result = None
    while not stop:
        instr = input("> ")
        split_instr = instr.split(" ")
        try:
            if len(split_instr) == 2:
                x = int(split_instr[0])
                y = int(split_instr[1])
                result = f"Ouvrir la case {x}, {y}"
                stop = True
            elif len(split_instr) == 3 and split_instr[0] == "F":
                x = int(split_instr[1])
                y = int(split_instr[2])
                result = f"Flagger la case {x}, {y}"
                stop = True
            else:
                print("Commande invalide")
        except ValueError:
            print("Coordonées invalides")

    print(result)
    return result


def main():
    win = False
    loss = False
    while not win and not loss:
        ask_instr()

