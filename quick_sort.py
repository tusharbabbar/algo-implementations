from helpers import swap_in_array, is_sorted
from random import randint
from time import sleep

def split(a, starting_index, ending_index):
    """Splits the array into 2 such that the elements on right of the pivot are
    always greater and the elements on the left are lesser than the pivot.
    Given an array:
        1. Pick the last element in the array and put it on the first position
        (We start by considering pivot is initially at first position)
        2. Compare the element with each element such that:
            if element is less than pivot:
                Put the element on current pivot position.
                move the element next to pivot on i position.
                Increment pivot position by 1.
    Note that here we would want that the array divides into 2 equal halves.
    Then only we can expect logrithmic performace of quicksort.
    Consider the case of a sorted array. Since we always consider the last
    element to act as pivot element the algo will act like insertion sort.
    """
    pos = starting_index # Position of the pivot
    pivot = a[ending_index]
    swap_in_array(a, starting_index, ending_index)
    i = pos + 1
    while i < ending_index + 1:
        if a[i] < a[pos]:
            swap_in_array(a, pos, i)
            pos += 1
            swap_in_array(a, pos, i)
        i += 1
    return pos

def quick_sort(a, starting_index, ending_index):
    """Sorts an array using quick sort algorithm.
    Algorithm: Quick sort is a divide and conquer algo that can sort an array
    inplace. The algorithm relies on the split/partition subroutine to sort the
    given input.
    Given an unsorted array:
        1. Split the array into 2 such that all the elements on left of the
        pivot are smaller and others on right are greater than the pivot.
        2. Apply Quick sort on the divided sub arrays.
        3. Repeat till size of sub arrays is 1.
    
    The algorithm is O(n^2) and Omega(nlogn). This will depend on the pivot
    you select in the split subroutine. Refer to the Docstring for split
    function.
    """
    if ending_index > starting_index:
        pivot = split(a, starting_index, ending_index)
        quick_sort(a, starting_index, pivot-1)
        quick_sort(a, pivot + 1, ending_index)

if __name__ == '__main__':
    large_array = []
    for i in xrange(1,1000):
        large_array.append(randint(1, 40) + i)
    print is_sorted(large_array)
    quick_sort(large_array, 0, len(large_array) - 1)
    print is_sorted(large_array)
