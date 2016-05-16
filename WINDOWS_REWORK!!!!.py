import msvcrt


def getchar():
    b = None
    done = False
    while not done:
        if msvcrt.kbhit():
            b = str(msvcrt.getch())
            done = True
            return b[2:3]

print(getchar())