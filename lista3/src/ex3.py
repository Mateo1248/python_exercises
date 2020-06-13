import sys

def sum_last(path):
    with open(path) as file:
        return sum([float(line.split()[-1]) for line in file])

print(sum_last(sys.argv[1]))