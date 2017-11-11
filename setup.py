#!/usr/bin/env python

from setuptools import setup, find_packages
test_deps = [
    'nose'
]
extras = {
    'test': test_deps,
}

setup(
    name='regi_reporter',
    version='0.0.1',
    description='reporting module that takes data/results from different units and combines these.',
    long_description='we can create standard technical day/week/financial reports but we can also join, concatenate '
                     'and summarize data from various flocks. Besides this there is an api endpoint available to make '
                     'requests to generate these reports.',
    author='Vincent Claes',
    author_email="vincent.claes@porphyrio.com",
    license='',
    url='https://bitbucket.org/porphyrio/regi_reporter',
    scripts=['regi_reporter/bin/app', 'regi_reporter/bin/report', 'regi_reporter/bin/report.bat'],
    packages=find_packages(),
    package_data={
        '': ['*.json', '*.csv']
    },
    install_requires=[
        'pandas == 0.20.0',
        'matplotlib'
    ],
    tests_require=test_deps,
    extras_require=extras,
    zip_safe=False
)
