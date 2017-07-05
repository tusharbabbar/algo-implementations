from datetime import datetime

def timeit(func):
    def _decorate(*args, **kwargs):
        start_time = datetime.utcnow()
        returned_from_func = func(*args, **kwargs)
        print("time taken in {fname}={tdiff}".format(
            fname=func.__name__,
            tdiff=str(datetime.utcnow() - start_time)))
        return returned_from_func
    return _decorate

def swap_in_array(array, i, j):
    temp = array[i]
    array[i] = array[j] 
    array[j] = temp

def is_sorted(a):
    return all([a[i] <= a[i+1] for i in range(0, len(a)-1)])
