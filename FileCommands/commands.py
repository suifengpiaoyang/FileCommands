import argparse
import fnmatch
import os
import shutil
import sys

from functools import partial


def zcopy():
    parser = argparse.ArgumentParser(
        description='copy files to destination'
    )
    parser.add_argument('src', help='source, can be file or folder')
    parser.add_argument('dst', help='destination')
    args = parser.parse_args()
    src = os.path.abspath(args.src)
    dst = os.path.abspath(args.dst)
    if os.path.isdir(src):
        if os.path.isdir(dst):
            shutil.copy2(src, dst)
        else:
            print(f'Error: [{dst}] must be a directory!')
            sys.exit()
    else:
        path = os.path.dirname(src)
        pattern = os.path.basename(src)
        if not os.path.exists(path):
            print(f'Error: [{path}]: No such path!')
            sys.exit()
        names = os.listdir(path)
        matches = fnmatch.filter(names, pattern)
        nums = len(matches)
        if nums == 0:
            pass
        elif nums == 1:
            filepath = os.path.join(path, matches[0])
            shutil.copy2(filepath, dst)
        else:
            if not os.path.isdir(dst):
                print(f'Error: [{dst}] not a directory!')
                sys.exit()
            for file in matches:
                filepath = os.path.join(path, file)
                shutil.copy2(filepath, dst)

def zmove():
    pass
