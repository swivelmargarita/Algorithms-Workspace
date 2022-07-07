import helpers
import quick_sort_hoare
import quick_sort
import time


def test_quick_sort(n=100):
    avg_time=0
    for i in range(n):
        start=time.process_time()
        A = helpers.random_list(10**4, low=-10**6, high=10**6)
        quick_sort.sort(A)
        avg_time+=time.process_time()-start
        assert helpers.is_sorted(A), f"Sequence is not sorted{A}"
    print(f"Successful with average time of {avg_time/n}")

def test_quick_sort_hoare(n=100):
    avg_time=0
    for i in range(n):
        start=time.process_time()
        A = helpers.random_list(10**4, low=-10**6, high=10**6)
        quick_sort_hoare.sort(A)
        avg_time+=time.process_time()-start
        assert helpers.is_sorted(A), f"Sequence is not sorted{A}"
    print(f"Successful with average time of {avg_time/n}")


if __name__ == '__main__':
    test_quick_sort()
    test_quick_sort_hoare()
