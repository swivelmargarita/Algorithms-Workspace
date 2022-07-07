import helpers


#Hoare Method
def partition(A, l, r, is_reverse=False):
    if(helpers.is_all_equal(A[l:r+1])):
        return (l+r)//2
    x=A[l]
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
        else:
            return j

def quick_sort(A, l, r, is_reverse=False) -> None:
    if l<r:
        q=partition(A, l, r, is_reverse)
        quick_sort(A, l, q, is_reverse)
        quick_sort(A, q+1, r, is_reverse)

def sort(A):
    quick_sort(A, 0, len(A)-1)
