import argparse
import os
import re
from typing import Sequence


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    parser.add_argument(
        '-r', '--regexp',
        help='Branch regexp',
        required=True
    )
    args = parser.parse_args(argv)

    branch = os.popen("git rev-parse --abbrev-ref HEAD").read()
    pattern = re.compile(args.regexp)

    match = re.search(pattern, branch)
    if match:
        return 0
    return 1
    
if __name__ == '__main__':
    raise SystemExit(main())