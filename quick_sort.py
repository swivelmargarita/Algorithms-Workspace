import random 
import sys
from itertools import groupby

def all_equal(iterable) -> bool:
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def partition(A, l, r, is_reverse=False) -> int:
    if(all_equal(A[l:r+1])):
            return (l+r)//2
    x = A[r] # Pivot
    i = l-1 # Rightmost element that smaller than pivot
    if(not is_reverse):
        for j in range(l, r):
            if A[j]<=x: # If current item belongs to left side of the pivot, swap 
                i+=1 # it with the rightmost element s.t. larger than pivot
                A[j], A[i] = A[i], A[j] # Swapping action
        A[i+1], A[r] = A[r], A[i+1] # Place the pivot in the right place
    else:
        for j in range(l, r):
            if A[j]>=x:
                i+=1
                A[j], A[i] = A[i], A[j] # Swapping action
        A[i+1], A[r] = A[r], A[i+1] # Place the pivot in the right place
    return i+1

def hoare_partition(A, l, r, is_reverse=False):
    x=A[l]
    print(f"\nNew function call. x is {x}, l is {l+1}, r is {r+1} ")
    i=l-1
    j=r+1
    while True:
        while True:
            j-=1
            if A[j]<=x:
                break
        while True:
            i+=1
            if A[i]>=x:
                break
        if i<j:
            A[i], A[j] = A[j], A[i]
            print(f"Swapped {A[i]} with {A[j]}: ", *A)
        else:
            print(f"Returning j:{j+1}")
            return j

def quick_sort(A, l, r, is_reverse=False) -> None:
    if l<r:
        #q = partition(A, l, r, is_reverse)
        q=hoare_partition(A, l, r, is_reverse)
        quick_sort(A, l, q, is_reverse)
        quick_sort(A, q+1, r, is_reverse)

sys.setrecursionlimit(10**5)
A=[random.randint(1,7) for i in range(7)]
A=[5,7,6,4,3,5,4]
A=[13,19,9, 5,12,8, 7,4, 11,2, 6,21]
print(*A)
quick_sort(A, 0, len(A)-1)
if(not (sorted(A)==A)):
    print("Your shit stinks. Sort again: ", *A)
