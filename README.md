# SALES REPORT

this is a test project that generates a sales report with images
and tables using python, pandas and jinja2.

## Install

this is tested on ubuntu. the generation of images with matplotlib might cause issues on windows

 prerequisites for installing matplotlib on ubuntu:

 `sudo apt-get install libfreetype6-dev`

 to install this python module execute the following command

 `pip install -r requirements.txt`

## USAGE

### monthly report

execute the following command:

`report monthly`

the default month is the last month. If you want to select the report for 2 months ago, execute

`report monthly --month 2`


## Tests

no tests are written.