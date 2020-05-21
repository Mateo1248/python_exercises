import argparse
import os

def dir_name_to_lower_rec(path):
    _all = []
    for root, dirs, files in os.walk(path,topdown=False):
        for name in files:
          _all.append(os.path.join(root, name))
        for name in dirs:
            _all.append(os.path.join(root, name))
    
    _all.sort()

    for i in range(len(_all)):
        os.rename(_all[i], _all[i].lower())
        last_changed = _all[i]
        for j in range(len(_all)):
            _all[j] = _all[j].replace(last_changed, last_changed.lower())


parser = argparse.ArgumentParser(description='Change subfolder names to lowercase recursively.')
parser.add_argument('path', type=str, help='Path to folder.')

args = parser.parse_args()

dir_name_to_lower_rec(args.path)
