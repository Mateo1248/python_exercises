import sys

def qsort(arr):
    if arr:
        elts_lt_x = filter(lambda x: x < arr[0], arr[1:])
        elts_greq_x = filter(lambda x: x >= arr[0], arr[1:])
        return qsort(list(elts_lt_x)) + arr[0] + qsort(list(elts_greq_x))
    return ''

print(qsort(sys.argv[1]))