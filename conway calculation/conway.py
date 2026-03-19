# wsl; conda activate sage

from sage.all import *
from sage.plot import *

# word for braid
braids = {
    "2 original": [1, 1, -1, -1, 2, 2],
    "2 transformed": [1, 1, -2, -2, -1, -1, 2, 2],
    "3 original": [1, 1, -1, -1, 2, 2, -2, -2, 3, 3],
    "3 transformed": [1, 1, -1, -1, 2, 2, -3, -3, -2, -2, 3, 3],
    "4 original": [1, 1, -1, -1, 2, 2, -2, -2, 3, 3, -3, -3, 4, 4],
    "4 transformed": [1, 1, -1, -1, 2, 2, -2, -2, 3, 3, -4, -4, -3, -3, 4, 4]
}

for name, word in braids.items():
    print(name, ":")
    # counts number of strands, based on word
    k = int(max(abs(i) for i in word) + 1)

    B = BraidGroup(k)
    b = B(word)
    print("Number of strands:" ,b.components_in_closure())
    B(word).plot().save(f"{name}_braid.png")

    L = Link(b)
    print("Number of components",L.number_of_components())
    L.plot().save(f"{name}_link.png")

    print("Conway polynomial:", L.conway_polynomial())