import numpy as np

def mean(alist):
    """
    Calculate the mean value of a given list of numbers.

    Args:
        alist (list): A list of numbers.

    Returns:
        float: The mean value of the input list.
    """
    alist = np.array(alist)
    tot_items = alist.shape[0]
    print(tot_items)
    return sum(alist)/tot_items