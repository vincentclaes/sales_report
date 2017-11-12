@echo off & python -x "%~f0" %* & goto :eof
# this can be used on windows as entry point
from sales_report.cli import get_parser

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    args.func(args)
