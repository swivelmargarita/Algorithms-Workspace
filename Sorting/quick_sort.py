import helpers


def partition(A, l, r, is_reverse=False) -> int:
    if(helpers.is_all_equal(A[l:r+1])):
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

def quick_sort(A, l, r, is_reverse=False) -> None:
    if l<r:
        q = partition(A, l, r, is_reverse)
        quick_sort(A, l, q-1, is_reverse)
        quick_sort(A, q+1, r, is_reverse)

def sort(A, is_reverse=False):
    quick_sort(A, 0, len(A)-1, is_reverse)
