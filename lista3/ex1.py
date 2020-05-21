def transpose(arr):
    length = len(arr) 
    return [" ".join([row.split()[col] for row in arr]) for col in range(length)]

print(transpose(["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]))