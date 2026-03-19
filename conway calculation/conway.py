# wsl; conda activate sage

from sage.all import *
from sage.plot import *

# word for braid
word = [1, 1] # change this obviously

# counts number of strands, based on word
k = int(max(abs(i) for i in word) + 1)

B = BraidGroup(k)
L = Link(B(word))

# print("strands:", strands)
print(B(word).components_in_closure())
print(L.number_of_components())
print("Conway polynomial:", L.conway_polynomial())
p = L.plot()
p.save("link.png")