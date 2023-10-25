import numpy as np

def mean(alist):
    alist = np.array(alist)
    tot_items = alist.shape[0]
    print(tot_items)
    return sum(alist)/tot_items