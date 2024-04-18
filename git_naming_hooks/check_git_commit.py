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
    parser.add_argument('message') 
    args = parser.parse_args(argv)

    pattern = re.compile(args.regexp)
    message = args.message
    
    print(f"We match pattern {pattern} with message commit '{message[:5]}...'.")

    match = re.search(pattern, message)
    if match:
        print("Commit message is correct.")
        return 0
    
    print("Commit message has not correct format.")
    return 1
    
if __name__ == '__main__':
    raise SystemExit(main())