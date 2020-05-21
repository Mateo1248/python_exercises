def power_set(arr):
    if arr:
        power_rec = power_set(arr[1:])
        return list(map(lambda x : [arr[0]] + x, power_rec)) + power_rec
    else:
        return [[]]

print(power_set([1,2,3]))