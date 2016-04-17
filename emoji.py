import random

COUNT = 1000
FILE = "emojis.txt"

emojis = (
    list(range(0x1F601, 0x1F64F + 1))
    + list(range(0x1F601, 0x1F64F + 1))
    + list(range(0x2702, 0x27B0 + 1))
    + list(range(0x1F680, 0x1F6C0 + 1))
    + list(range(0x24C2, 0x1F251 + 1))
    + list(range(0x1F600, 0x1F636 + 1))
    + list(range(0x1F681, 0x1F6C5 + 1))
    + list(range(0x1F30D, 0x1F567 + 1))
    + list(range(0x1F30D, 0x1F567 + 1))
)

listlength = len(emojis)
rand = random.randrange
with open(FILE, "w", encoding="utf8") as f:
    f.write(str(COUNT) + " Emojis\n")
    for i in range(COUNT):
        char = chr(emojis[rand(listlength - 1)])
        f.write(char + " ")