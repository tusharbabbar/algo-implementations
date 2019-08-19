def get_subset_sum(inputs, total):
    """Bottom Up solution
        If total is zero
            return Exists with no input to be considered
        If inputs is empyt
            return no solution exists
        If last element of the inputs array is greater than total
            Do not consider the last element and try for other elements
        if last element is lesser than or equat to total
            check if solution exists with considering the last element
                if not
                    Do not consider the last element
    """
    if total == 0:
        return True, []
    if not inputs:
        return None, []
    last = inputs[-1]
    if last > total:
        return get_subset_sum(inputs[:-1], total)
    else:
        exists, summing_input = get_subset_sum(inputs[:-1], total - last)
        if exists:
            return True, summing_input + [last]
        else:
            return get_subset_sum(inputs[:-1], total)

if __name__ == "__main__":
    inputs = [2, 3, 7, 8, 10]
    total = 10
    print(get_subset_sum(inputs, total))

