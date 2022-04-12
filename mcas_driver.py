

import os.path

import requests
import pandas as pd
import sys, getopt
from bs4 import BeautifulSoup
from os.path import join, isdir, abspath, pathsep
from mcas_library import *



report = MCASExtract("https://profiles.doe.mass.edu/statereport/mcas.aspx")

output_directory = "outdir"
# report.print_report_options()

req_params = dict()
req_params['ctl00$ContentPlaceHolder1$ddReportType'] = ['DISTRICT']
req_params['ctl00$ContentPlaceHolder1$ddYear'] = ['2018', '2017', '2016', '2015', '2014']
req_params['ctl00$ContentPlaceHolder1$ddGrade'] = ['AL']
req_params['ctl00$ContentPlaceHolder1$ddSchoolType'] = ['ALL']
req_params['ctl00$ContentPlaceHolder1$ddSubGroup'] = ['AL:AL']
req_params['ctl00$ContentPlaceHolder1$hfExport'] = "Excel"

# req_params['ctl00$ContentPlaceHolder1$ddSubGroup23'] = ['SHOOOT']

try:

    param2 = dict()
    for a in req_params['ctl00$ContentPlaceHolder1$ddReportType']:
        for b in req_params['ctl00$ContentPlaceHolder1$ddYear']:
            for c in req_params['ctl00$ContentPlaceHolder1$ddGrade']:
                for d in req_params['ctl00$ContentPlaceHolder1$ddSchoolType']:
                    for e in req_params['ctl00$ContentPlaceHolder1$ddSubGroup']:
                        param2['ctl00$ContentPlaceHolder1$ddReportType'] = a
                        param2['ctl00$ContentPlaceHolder1$ddYear'] = b
                        param2['ctl00$ContentPlaceHolder1$ddGrade'] = c
                        param2['ctl00$ContentPlaceHolder1$ddSchoolType'] = d
                        param2['ctl00$ContentPlaceHolder1$ddSubGroup'] = e

                        report.get_report_real(parameters=param2)
                        report.remove_header_row()
                        # now add a year column
                        report.add_column(0, 'Year', '2001')
                        filenamebase = "{}-{}-{}-{}-{}.csv".format(a, b, c, d, e)
                        filenamebase = os.path.join(output_directory, filenamebase)
                        report.write_csv(filenamebase)
except MCASException as e:
    print("Error: {}".format(e))
    exit(-1)
