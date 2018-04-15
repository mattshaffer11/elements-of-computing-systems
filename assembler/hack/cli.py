import os
import argparse

from .parser import parse


def main():
    parser = argparse.ArgumentParser(description='Translates Hack assembly language into binary code.')
    parser.add_argument('source', type=argparse.FileType('r'), help='source file')
    parser.add_argument(
        '-o',
        dest='output_path',
        help='output path, defaults to source file name with .hack extension'
    )
    parser.add_argument(
        '-s',
        dest='stdout',
        action='store_true',
        help='output results to stdout'
    )
    args = parser.parse_args()

    with args.source as source:
        code = parse(source.read())

    if args.stdout:
        print(code)
    elif args.output_path:
        with open(args.output_path, 'w') as f:
            f.write(code)
    else:
        with open(_translate_filename(args.source.name), 'w') as f:
            f.write(code)


def _translate_filename(filename):
    return os.path.splitext(filename)[0] + '.hack'


if __name__ == '__main__':
    main()
