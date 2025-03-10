#!/usr/bin/env python3

import sys
import yaml
import re
import argparse

# main
if __name__ == "__main__":
    # parse command-line
    ps = argparse.ArgumentParser()
    ps.add_argument('-i', '--input', action='store', default=None, help='YAML-formatted input variable file')
    ps.add_argument('-o', '--output', action='store', default="API.md", help='Markdown-formatted API documentation file')
    args = ps.parse_args()

    # check for args
    if args.input == None:
        sys.exit(1)

    errors_count = 0
    with open(args.input) as varfile:
        vars = yaml.safe_load(varfile.read())

        with open(args.output) as docfile:
            doc = docfile.read()
            for key in vars.keys():
                pattern = f'<!-- block {key} -->'
                match = re.search(pattern, doc)
                if not bool(match):
                    print(f'Found un-documented variable {key}, please update {args.output} file.')
                    errors_count += 1

    sys.exit(errors_count)
