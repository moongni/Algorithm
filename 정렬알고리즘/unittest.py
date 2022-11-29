from random import randint
from copy import copy
from selection_sort import selection_sort
from insertion_sort import insertion_sert, shell_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from counting_sort import counting_sort
from radix_sort import radix_sort
from heap_sort import heap_sort

if __name__ == "__main__":

    # selection sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        selection_sort(testcase2)
        testcase.sort()

        assert(testcase == testcase2)    


    # insertion sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        insertion_sert(testcase2)
        testcase.sort()
        assert(testcase == testcase2)

    # bubble sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        bubble_sort(testcase2)
        testcase.sort()
        assert(testcase == testcase2)

    # merge sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        merge_sort(testcase2)
        assert(testcase == testcase2)

    # quick sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        quick_sort(testcase2)
        assert(testcase == testcase2)

    # shell_sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        shell_sort(testcase2)
        assert(testcase == testcase2)

    # counting sort unit test
    for n in range(10):
        testcase = [randint(0, 30) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        testcase2 = counting_sort(testcase2)
        assert(testcase == testcase2)

    # radix sort unit test
    for n in range(10):
        testcase = [randint(0, 1001) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        radix_sort(testcase2)
        assert(testcase == testcase2)

    # heap sort unit test
    for n in range(10):
        testcase = [randint(0, 1001) for i in range(randint(1, 20))]
        testcase2 = copy(testcase)
        testcase.sort()
        heap_sort(testcase2)
        assert(testcase == testcase2)
