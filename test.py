import argparse
from os.path import dirname, realpath, relpath

from jinja2 import *

def parse_arguments():
    parser = argparse.ArgumentParser(description='Render a Jinja2 template.')
    parser.add_argument("input", help="Read from INPUT")
    parser.add_argument("output", nargs="?", default="-",
                        help="Write to OUTPUT (default: -)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    srcdir = '.' #dirname(realpath(args.input))
    env = Environment(loader=FileSystemLoader(srcdir),
                      autoescape=select_autoescape(('html', 'xml')),
                      trim_blocks=True,
                      undefined=StrictUndefined)
    with argparse.FileType('w', encoding="utf-8")(args.output) as output:
        output.write(env.get_template(relpath(args.input, srcdir)).render())

if __name__ == '__main__':
    main()
