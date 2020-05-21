def flatten(arr):
    if type(arr) is list:
        for i in iter(arr):
            for j in flatten(i):
                yield j
    else:
        yield arr

l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
print(list(flatten(l)))
