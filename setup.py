#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='sales_report',
    version='0.0.1',
    description='report from dataset using pandas and jinja2.',
    author='Vincent Claes',
    author_email="vclaes1986@gmail.com",
    scripts=['sales_report/report', 'sales_report/report.bat'],
    packages=find_packages(),
    package_data={
        '': ['*.xlsx', '*.pickle']
    },
    install_requires=[
        'pandas==0.20.0',
        'matplotlib==2.1.0',
        'jinja2==2.10',
        'jupyter==1.0.0',
        'xlrd'
    ],
)
