from collections import defaultdict
from itertools import product

with open("raw_data4.txt") as f:
    ls = f.read().strip().split("\n")

boardz = defaultdict(str)
boardz |= {i + 1j * j: x for i, l in enumerate(ls) for j, x in enumerate(l)}
octdir = {i + 1j * j for (i, j) in set(product((-1, 0, 1), (-1, 0, 1))) - {(0, 0)}}

res = 0
for z in list(boardz.keys()):
    if boardz[z] == "A":
        corners = [
            boardz[z + 1 + 1j],
            boardz[z + 1 - 1j],
            boardz[z - 1 - 1j],
            boardz[z - 1 + 1j],
        ]
        if (
            corners.count("M") == 2
            and corners.count("S") == 2
            and boardz[z - 1 - 1j] != boardz[z + 1 + 1j]
        ):
            res += 1
print(res)