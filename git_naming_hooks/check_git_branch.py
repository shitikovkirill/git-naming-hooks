import argparse
import os
from typing import Any
from typing import Sequence


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('regexps', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    branch = os.popen("git rev-parse --abbrev-ref HEAD").read()
    print(branch)
    print(args)
    return 1
    
if __name__ == '__main__':
    raise SystemExit(main())