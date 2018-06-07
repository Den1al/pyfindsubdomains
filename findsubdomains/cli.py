#!/usr/bin/env python

import sys

try:
    from findsubdomains import FindSubDomains
except ModuleNotFoundError:
    sys.path.append('../')
    from findsubdomains import FindSubDomains

from argparse import ArgumentParser, FileType
from pathlib import Path


def parse_args():
    parser = ArgumentParser()

    parser.add_argument("domain", help="the domain to look for")
    parser.add_argument(
        "-s", "--startswith", help="whether to look for subdomains that starts with", action="store_true")

    return parser.parse_args()


def main():
    args = parse_args()
    fsd = FindSubDomains(
        domain=args.domain,
        startswith=args.startswith
    )

    for result in fsd.get():
        print(result)


if __name__ == '__main__':
    main()
