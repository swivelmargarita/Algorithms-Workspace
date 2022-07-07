import helpers
from random import randint


def insertion_sort(A):
    n=len(A)
    for i in range(1, n):
        key=A[i]
        j=i-1
        while j>=0 and A[j]>=key:
            A[j+1]=A[j]
            j-=1
        A[j+1]=key


A=helpers.random_list(10, 0, 10)
print("Initial sequence: ", *A)
insertion_sort(A)
helpers.test_correctness(A)
