#Cobine data from multiple sources into a single result
from collections import Counter

def combinning_dicts(*dicts : dict) -> dict:

    unsorted_c = Counter()

    if not dicts:
        return None
    
    for d in dicts:
        unsorted_c.update(d)
    return dict(sorted(unsorted_c.items(), key = lambda tup: tup[1], reverse=True))


d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

consolidated_dict = combinning_dicts(d1,d2,d3)

print(consolidated_dict)

#{'python': 17, 'javascript': 15, 'java': 13, 'c#': 12, 'c++': 10, 'go': 9, 'erlang': 5, 'haskell': 2, 'pascal': 1}