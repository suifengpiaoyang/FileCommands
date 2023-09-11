import argparse
import fnmatch
import os
import shutil
import sys


from send2trash import send2trash


def _del(params, command_name=None):
    description = params.get('description')
    files_function = params['files_function']
    directory_function = params['directory_function']

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('src', help='source file path')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='delete files recursively')
    args = parser.parse_args()
    src = os.path.abspath(args.src)
    r_flag = args.recursive
    if os.path.isdir(src):
        if r_flag:
            print('Directory not supported -r parameter!' +
                  ' The file and directory has not changed.')
            return
        directory_function(src)
    else:
        path = os.path.dirname(src)
        pattern = os.path.basename(src)
        if not os.path.exists(path):
            print(f'Error: [{path}]: No such path!')
            sys.exit()
        if r_flag:
            if command_name == 'zdel':
                _f = input('Warnning! You try to delete files and the files '
                           'does not send to trash! Are you sure to do this?'
                           '(y/n, default n)')
                if _f not in ('y', 'Y'):
                    print('Not delete any files!')
                    return
            for root, dirs, files in os.walk(path):
                matches = fnmatch.filter(files, pattern)
                for file in matches:
                    filepath = os.path.join(root, file)
                    files_function(filepath)
        else:
            names = os.listdir(path)
            matches = fnmatch.filter(names, pattern)
            for file in matches:
                filepath = os.path.join(path, file)
                files_function(filepath)


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


def zdel():
    params = {
        'description': 'delete files or folder, not send to trash!',
        'files_function': os.remove,
        'directory_function': shutil.rmtree
    }
    _del(params, command_name='zdel')


def zrecycle():
    params = {
        'description': 'send files or folder to the trash',
        'files_function': send2trash,
        'directory_function': send2trash
    }
    _del(params)


def zlist():
    parser = argparse.ArgumentParser(
        description='list the file name which is matched'
    )
    parser.add_argument('pattern', help='the match pattern')
    parser.add_argument('-r',
                        '--recursive',
                        action='store_true',
                        help='delete files recursively')
    args = parser.parse_args()
    abspath = os.path.abspath(args.pattern)
    path = os.path.dirname(abspath)
    pattern = os.path.basename(abspath)
    if not os.path.exists(path):
        print(f'Error: [{path}]: No such path!')
        sys.exit()
    if args.recursive:
        for root, dirs, files in os.walk(path):
            matches = fnmatch.filter(files, pattern)
            for file in matches:
                filepath = os.path.join(root, file)
                print(filepath)
    else:
        names = os.listdir(path)
        matches = fnmatch.filter(names, pattern)
        for file in matches:
            print(file)
