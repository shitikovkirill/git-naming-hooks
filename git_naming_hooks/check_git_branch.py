import argparse
import os
import sys
from typing import Any
from typing import Sequence


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    branch = os.popen("git rev-parse --abbrev-ref HEAD").read()
    print(branch)
    print(args)
    print(sys.argv[:])
    return 1
    
if __name__ == '__main__':
    raise SystemExit(main())