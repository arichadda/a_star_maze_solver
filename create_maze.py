# Ari Chadda
# 3 October 2020
# PA2
import random

# generates random mazes, change sizes manually
if __name__ == "__main__":
    f = open("maze7.maz", "w")

    for value1 in range(8):
        if value1 > 0:
            f.write("#\n#")
        else:
            f.write("#")
        for value2 in range(4):
            if bool(random.getrandbits(1)):
                f.write("#.")
            else:
                f.write("..")


    f.close()