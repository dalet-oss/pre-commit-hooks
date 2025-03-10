from __future__ import annotations

import argparse
import sys
import yaml
import re

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', action='store', default=None, help='YAML-formatted input variable file')
    parser.add_argument('-o', '--output', action='store', default="API.md", help='Markdown-formatted API documentation file')
    args = parser.parse_args(argv)

    if args.input == None:
        return 1

    retval = 0
    try:
        with open(args.input) as varfile:
            vars = yaml.safe_load(varfile.read())

            with open(args.output) as docfile:
                doc = docfile.read()
                for key in vars.keys():
                    pattern = f'<!-- block {key} -->'
                    match = re.search(pattern, doc)
                    if not bool(match):
                        print(f'Found un-documented variable {key}, please update {args.output} file.')
                        retval += 1
    except SyntaxError as e:
        print(e)
        retval = 1

    return retval

if __name__ == '__main__':
    raise SystemExit(main())
