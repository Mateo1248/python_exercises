import argparse
import os
import hashlib
import bitstring

def find_duplicates(path):
    file_stats = []
    file_names = []
    for root, dirs, files in os.walk(path,topdown=False):
        for f_name in files:
            with open (os.path.join(root, f_name), "rb") as file:
                fileStr =  file.read()
                stat = (hashlib.md5(fileStr).hexdigest(), os.stat(os.path.join(root, f_name)).st_size)
                if file_stats.count(stat) > 0:
                    file_names[file_stats.index(stat)].append(os.path.join(root, f_name))
                else:
                    file_names.append([os.path.join(root, f_name)])
                    file_stats.append(stat)
    
    for duplicates in [x for x in file_names if len(x) > 1]:
        print('-------------------------------')
        for d in duplicates:
            print(d)
    print('-------------------------------')


parser = argparse.ArgumentParser(description='Find duplicates recursively.')
parser.add_argument('path', type=str, help='Path to folder.')

args = parser.parse_args()

find_duplicates(args.path)