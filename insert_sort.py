from helpers import swap_in_array, timeit

def insert_sort(unsorted):
    '''Sorts a given list inplace using Insertion Sort Algo.
    Algorithm: Consider that the array is divided in to 2 subarrays, Left
    and Right. Array on Left is sorted while the Right is unsorted. In order
    to sort the array we pick an element from the Right. And put its correct
    place in Left. Thus in the end all the elements on the Left side become
    sorted.

    Initially Left has only 1 element. Thus sorted.
    While there are elements in Right:
        1. Pick first element on Right say E.
        2. Move from right to left in Left array.
        3. On each step compare the element on that step with E.
        4. If E is smaller than element on that step swap element on step with
           the next element. i.e. step + 1 position.
        4. If E is greater than the element on that step stop the iteration.

    This is an O(n**2) algorithm.
    The algo is decent to be used for an array of length 30.

    Best Case: Sorted Array. O(n).
    Worst Case: Reverse Sorted Array. O(n**2).
    '''
    for i in range(1, len(unsorted)):
        element = unsorted[i]
        j = i-1
        while j >= 0:
            if unsorted[j] > element:
                swap_in_array(unsorted, j, j+1)
            else:
                break
            j -= 1
        unsorted[j+1] = element

@timeit
def best_case():
    # sorted array
    a = list(xrange(30))
    insert_sort(a)
    print a

@timeit
def worst_case():
    # reverse sorted array
    a = list(xrange(30))
    a.reverse()
    insert_sort(a)
    print a


if __name__ == '__main__':
    best_case()
    worst_case()
