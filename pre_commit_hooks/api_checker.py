from __future__ import annotations

import argparse
import sys
import yaml
import re

def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)

    if args.input == None:
        return 1

    retval = 0
    for filename in args.filenames:
        try:
            with open(filename) as varfile:
                vars = yaml.safe_load(varfile.read())

                with open('API.md') as docfile:
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
