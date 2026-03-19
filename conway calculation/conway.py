from sage.all import *
from sage.plot import *
from braids import braids

for name, word in braids.items():
    print(name, ":")
    # counts number of strands, based on word
    k = int(max(abs(i) for i in word) + 1)

    B = BraidGroup(k)
    b = B(word)
    print("Number of strands:" ,b.components_in_closure())
    B(word).plot(orientation = "top-bottom").save(f"{name}_braid.png")

    L = Link(b)
    print("Number of components",L.number_of_components())
    L.plot().save(f"{name}_link.png")

    print("Conway polynomial:", L.conway_polynomial())