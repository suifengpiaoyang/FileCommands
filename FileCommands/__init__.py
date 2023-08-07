import argparse

from .commands import *


def main():
    parser = argparse.ArgumentParser(
        description='supply some file commands for different system',
        epilog='type <command> -h for more details'
    )
    parser.add_argument('-l',
                        '--list',
                        action='store_true',
                        help='list all the supported commands')
    args = parser.parse_args()
    supported_commands = ['zcopy', 'zmove']
    if args.list:
        print('Supported Commands:\n')
        for command in supported_commands:
            print(command)
        print('\ntype <command> -h for more details')
