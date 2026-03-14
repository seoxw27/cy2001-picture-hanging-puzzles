# wsl; conda activate sage

from sage.all import *

# word for braid
word = [2, 1, 1, 2, -1, 1] # change this obviously

# counts number of strands, based on word
k = max(abs(i) for i in word) + 1

B = BraidGroup(k)
b = B(word)
L = Link(b)

# print("strands:", strands)
print("Conway polynomial:", L.conway_polynomial())