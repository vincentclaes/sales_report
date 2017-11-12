import argparse
import os

from sales_report import ROOT
from sales_report.monthly import MonthlyReport
from view import generator

default_dataset = os.path.join(ROOT, 'data', 'Exercice_SalesData.xlsx')
default_template = os.path.join(ROOT, 'view', 'sales_report.html')
default_output = os.path.join(ROOT, 'view', 'output')


def monthly(args):
    """
    create monthly sales report
    :param args: cli arguments
    :return: None
    """
    d = MonthlyReport(args.dataset, args.month, args.path)
    template_vars = d.describe_past_month()
    generator.create_html_report(template_vars, args.template, args.path)


def get_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='sub-command help')
    ht = "create a report"
    parser_description = subparsers.add_parser('monthly', help=ht)
    parser_description.add_argument('--month', type=int, default=-1,
                                    help="define how many months ago you want to check")
    parser_description.add_argument('--dataset', type=str, default=default_dataset,
                                    help="the path to the dataset")
    parser_description.add_argument('--path', type=str, default=default_output,
                                    help="the output path of the report.")
    parser_description.add_argument('--template', type=str, default=default_template,
                                    help="the path of the template")
    parser_description.set_defaults(func=monthly)

    return parser
