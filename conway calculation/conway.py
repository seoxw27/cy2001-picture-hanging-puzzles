# wsl; conda activate sage

from sage.all import *

# word for braid
word = [1, 1] # change this obviously

# counts number of strands, based on word
k = int(max(abs(i) for i in word) + 1)

B = BraidGroup(k)
L = Link(B(word))

# print("strands:", strands)
print("Conway polynomial:", L.conway_polynomial())