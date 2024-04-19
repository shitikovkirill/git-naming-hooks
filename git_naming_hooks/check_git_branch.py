import argparse
import os
import re
from typing import Sequence


def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to check.")
    parser.add_argument("-r", "--regexp", help="Branch regexp", required=True)
    args = parser.parse_args(argv)

    pattern = re.compile(args.regexp)
    branch = os.popen("git rev-parse --abbrev-ref HEAD").read()

    print(f"We match pattern {pattern} with branch '{branch}'.")

    match = re.search(pattern, branch)
    if match:
        print("Branch is correct.")
        return 0

    print("Branch has not correct format.")
    return 1
