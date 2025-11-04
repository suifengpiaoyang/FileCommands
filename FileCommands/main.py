import argparse

from .commands import *


def main():
    parser = argparse.ArgumentParser(
        description='provides a set of user-friendly file manipulation '
        'commands to simplify common file management tasks',
        epilog='type <command> -h for more details'
    )
    parser.add_argument(
        '-l',
        '--list',
        action='store_true',
        help='list all the supported commands'
    )
    args = parser.parse_args()
    supported_commands = [
        'zcopy', 'zmove', 'zdel', 'zrecycle', 'zlist'
    ]
    if args.list:
        print('Supported Commands:\n')
        for command in supported_commands:
            print(command)
        print('\ntype <command> -h for more details')
