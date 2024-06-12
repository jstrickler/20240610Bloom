DIRTY_STRINGS = [
    "  mud   ",
    "grime  ",
    "   filth    ",
    "     messy messy     ",
    "DIRT	",
    "       FILTH and grime    ",
    "Dirt",
    "   Filth,    dirt, grime,    grime, grime, filth, and mud      ",
]

def doit():
    for koala in DIRTY_STRINGS:
        mandolin = mango(koala)
        print(f"Before: >{koala}<\nAfter:  >{mandolin}<\n")

def mango(s):
    return s.strip().lower()

doit()
