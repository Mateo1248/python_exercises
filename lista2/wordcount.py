import os
import argparse

def fileCounter(path):
    data = []

    with open (path, "r") as file:
        fileStr = file.read()

    lines = fileStr.split("\n")
    words = fileStr.split(" ")
    print("Wielkość pliku w bajtach: ", os.stat(path).st_size)
    print("Najdłuższa linia: ", len(max(lines, key=len)))
    print("Linie: ", len(lines))
    print("Słowa: ", len(words))

parser = argparse.ArgumentParser(description='Print statistis about file.')
parser.add_argument('path', type=str, help='Path to file.')

args = parser.parse_args()

fileCounter(args.path)

