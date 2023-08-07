import argparse
import fnmatch
import os
import shutil
import sys


def _copy(params):
    # extract params
    description = params.get('description')
    files_function = params['files_function']
    directory_function = params['directory_function']

    # main function
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('src', help='source, can be file or folder')
    parser.add_argument('dst', help='destination')
    args = parser.parse_args()
    src = os.path.abspath(args.src)
    dst = os.path.abspath(args.dst)
    if os.path.isdir(src):
        if os.path.isdir(dst):
            basename = os.path.basename(src)
            target = os.path.join(dst, basename)
            directory_function(src, target)
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
            files_function(filepath, dst)
        else:
            if not os.path.isdir(dst):
                print(f'Error: [{dst}] not a directory!')
                sys.exit()
            for file in matches:
                filepath = os.path.join(path, file)
                files_function(filepath, dst)


def zcopy():
    params = {
        'description': 'copy files to destination',
        'files_function': shutil.copy2,
        'directory_function': shutil.copytree
    }
    _copy(params)


def zmove():
    params = {
        'description': 'move files to destination',
        'files_function': shutil.move,
        'directory_function': shutil.move
    }
    _copy(params)
