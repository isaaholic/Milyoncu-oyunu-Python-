import time
def loading():
    bar = [
        " đŽ",
        " đŽđ˛",
        " đŽđ˛đšī¸",
        " đŽđ˛đšī¸đ",
        " đŽđ˛đšī¸",
        " đŽđ˛",
        " đŽ",
        " Created",
        "         by  ",
        "            Isa Memmedli",
    ]

    for i in range(30):
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        