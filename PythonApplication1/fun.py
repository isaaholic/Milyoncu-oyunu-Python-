import time
def loading():
    bar = [
        " 🎮",
        " 🎮🎲",
        " 🎮🎲🕹️",
        " 🎮🎲🕹️🏆",
        " 🎮🎲🕹️",
        " 🎮🎲",
        " 🎮",
        " Created",
        "         by  ",
        "            Isa Memmedli",
    ]

    for i in range(30):
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        