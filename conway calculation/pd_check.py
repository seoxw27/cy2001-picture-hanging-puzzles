from collections import Counter
from links import links

def check_pd_code(pd, name=""):
    # Flatten all labels
    labels = [x for crossing in pd for x in crossing]
    counts = Counter(labels)
    
    # Find problematic labels
    bad = {k: v for k, v in counts.items() if v != 2}
    
    if bad:
        print(f"\n{name} Invalid PD code")
        for k in sorted(bad):
            print(f"  Label {k} appears {bad[k]} times")
        return False
    else:
        print(f"{name} Valid PD code")
        return True


# Loop through your links
for name, pd in links.items():
    check_pd_code(pd, name)