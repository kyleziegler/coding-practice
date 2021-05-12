# Kyle Ziegler 2021
# QuickSort
# O(N^2)

# == Pseudo code example ==

import random
import math


# Recursive algorithm
def quick_sort(l:list)->list:
    larger = smaller = []


    if (len(l) > 1):
        pivot = l[math.floor(random.random() * len(l))]
        # pivot = l[0]
        print(pivot)
        for item in l:
            if (item < pivot):
                smaller.append(item)
            elif (item > pivot):
                larger.append(item)
        # quick_sort(smaller)
        # quick_sort(larger)
    else:
        return []
    
    return quick_sort(smaller) + [pivot] + quick_sort(larger)

print(quick_sort([9,6,3,5]))