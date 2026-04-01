from sage.all import *
from sage.plot import *
from links import links
import time
import sys

sys.setrecursionlimit(1000)

total = len(links)
start_time = time.time()

for name, data in links.items():
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