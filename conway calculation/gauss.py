from sage.all import *

links = {
    "2 original": [[[-1, 2, -3, -6, 7, 8, 9, -10, -8, 3, -4, 5, 6, -7],
                    [1, 10, -9, -2],
                    [4, -5]],
                   [1, 1, -1, 1, -1, 1, 1, -1, -1, -1]],
    "2 transformed": [[[-1, 2, 3, -9, -6, 5, -4, -3, 10, -11, 9, -8, 7, 6],
                       [1, 11, -10, -2],
                       [4, 8, -7, -5]],
                      [1, 1, -1, -1, -1, 1,
                       1, 1, -1, -1, -1]]
}

for name, data in links.items():
    print(data)
    L = Link(data)
    print(name, L)
    
    L.plot().save(f"{name}_gauss.pdf")

    #print("Conway polynomial:", L.conway_polynomial())