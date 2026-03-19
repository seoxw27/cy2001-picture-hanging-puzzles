# wsl; conda activate sage

from sage.all import *
from sage.plot import *

# word for braid
word = [1, 1, -1, -1, 2, 2, -3, -3, -2, -2, 3, 3] # change this obviously

# word = [1, 1, -1, -1, 2, 2, -2, -2, 3, 3]

# counts number of strands, based on word
k = int(max(abs(i) for i in word) + 1)

B = BraidGroup(k)
b = B(word)
print("Number of strands:" ,b.components_in_closure())
B(word).plot().save("braid.png")

L = Link(b)
print("Number of components",L.number_of_components())
L.plot().save("link.png")

print("Conway polynomial:", L.conway_polynomial())