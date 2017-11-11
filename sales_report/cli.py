import argparse
import os
from tempfile import mkdtemp

from sales_report import ROOT
from sales_report.description import Description
from view import generator

default_dataset = os.path.join(ROOT, 'data', 'Exercice_SalesData.xlsx')
temp_dir = mkdtemp(prefix='axa_test_')


def description(args):
    d = Description(args.dataset, args.month, args.path)
    template_vars = d.describe_past_month()
    generator.render_template_from_string(template_vars,
                                          r'/home/vagrant/Desktop/axa_test/axa_test/view/sales_report.html')


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help')
    ht = "create a report"
    parser_description = subparsers.add_parser('description', help=ht)
    parser_description.add_argument('--month', type=int, default=-1,
                                    help="define how many months ago you want to check")
    parser_description.add_argument('--dataset', type=str, default=default_dataset,
                                    help="define how many months ago you want to check")
    parser_description.add_argument('--path', type=str, default=temp_dir,
                                    help="define how many months ago you want to check")
    parser_description.set_defaults(func=description)

    return parser
