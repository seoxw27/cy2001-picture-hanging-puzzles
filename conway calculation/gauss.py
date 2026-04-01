from sage.all import *
from sage.plot import *
import sys
import time

sys.setrecursionlimit(2000)

links = {
    "2 original": [[[-1, 2, -3, -6, 7, 8, 9, -10, -8, 3, -4, 5, 6, -7],
                    [1, 10, -9, -2],
                    [4, -5]],
                   [1, 1, -1, 1, -1, 1, 1, -1, -1, -1]],
    "2 transformed": [[[-1, 2, 3, -9, -6, 5, -4, -3, 10, -11, 9, -8, 7, 6],
                       [1, 11, -10, -2],
                       [4, 8, -7, -5]],
                      [1, 1, -1, -1, -1, 1,
                       1, 1, -1, -1, -1]],
    "2 original wo self": [[[-1, 2, 5, -6, -3, 4],
                    [1, 6, -5, -2],
                    [3, -4]],
                   [1, 1, 1, -1, -1, -1]],
    "2 transformed wo self": [[[-1, 2, 4, -3, 7, -8, -6, 5],
                       [1, 8, -7, -2],
                       [3, 6, -5, -4]],
                      [1, 1, -1, -1, 1, 1, -1, -1]]
}

total = len(links)
start_time = time.time()

for name, data in links.items():
    print(f"\nProcessing {i}/{total}: {name}")
    print(data)

    L = Link(data)
    print(name, L)

    try:
        print(L.braid())
    except Exception as e:
        print("Failed to compute braid:", e)

    try:
        L.plot().save(f"{name}_gauss.pdf")
    except Exception as e:
        print("Failed to save link:", e)

    try:
        print("Conway polynomial:", L.conway_polynomial())
    except Exception as e:
        print("Failed to compute Conway polynomial:", e)

    # Progress + ETA
    elapsed = time.time() - start_time
    avg_time_per_iter = elapsed / i
    remaining_iters = total - i
    eta = avg_time_per_iter * remaining_iters

    print(f"Progress: {i}/{total}")
    print(f"Elapsed time: {elapsed:.2f}s")
    print(f"Estimated time remaining: {eta:.2f}s")