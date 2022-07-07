from random import randint
from itertools import groupby
def is_sorted(A) -> bool:
    n=len(A)
    for i in range(n-1):
        if A[i]>A[i+1]:
            return False
            break
    return True

def random_list(n, low=0, high=10**2):
    return [randint(low, high) for i in range(n)]

def test_correctness(A):
    if not is_sorted(A):
        print("Sequence is NOT sorted", *A)


def insertion_sort_qs(A, l, r) -> None:
    if l>r:
        for i in(l+1, r):
            key=A[i]
            j=i-1
        while j>=0 and A[j]>=key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key

def is_all_equal(iterable) -> bool:
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
