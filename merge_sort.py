from helpers import timeit
from insert_sort import insert_sort
from random import randint

def merge(sorted1, sorted2):
    '''Merges 2 sorted array into a single sorted array.
    Recursion: Given 2 sorted arrays
    1. Compare the top elements of both arrays and append the smaller element
    in auxillary array.
    2. Update the top of array with smaller element to top + 1.
    Repeat till we have iterated over all the elements of both the array.
    Dry run: 
        Given -- A= [1,3], B= [2,4], C= []
        Initially -- ta= 0, tb= 0
            Step1: A[ta] < B[tb]
                C= [1], ta= 1, tb= 0
            step2: A[ta] > B[tb]
                C= [1,2], ta= 1, tb= 1
    '''
    merged = []
    i,j = 0,0
    while i < len(sorted1):
        while(j < len(sorted2) and sorted2[j] < sorted1[i]):
            merged.append(sorted2[j])
            j += 1
        merged.append(sorted1[i])
        i += 1
    while j < len(sorted2):
        merged.append(sorted2[j])
        j += 1
    return merged

def mergesort(unsorted):
    '''Sort an array using merge sort algorithm
    Algorithm: Merge sort is a divide and conquer algorithm and it uses
    auxillary array to sort. Merge sort relys on subroutine called `Merge`
    to sort a given array.
    Given an unsorted array:
        1. If length of array is 1, return. Since single element is always
        sorted
        2. If length > 1, divide the array into 2 parts and sort both using
        a sorting technique(in this case we use mergesort itself) and return
        the merged sorted array using Merge subroutine.
    This will recursively sort the array.

    This is an O(nlogn) algorithm.
    The Worst Case and Best Case for this algorithm is the same.
    '''
    if len(unsorted) == 1:
        return unsorted
    else:
        split = len(unsorted)/2
        return merge(mergesort(unsorted[0:split]), mergesort(unsorted[split:]))

@timeit
def insertion_sort(a):
    insert_sort(a)

@timeit
def domergesort(a):
    mergesort(a)

if __name__ == '__main__':
    large_array = []
    for i in xrange(1,1000000):
        large_array.append(randint(999, 9999999) + i)
    print "Comparing merge and insertion sort"
    domergesort(large_array)
    insertion_sort(large_array)

