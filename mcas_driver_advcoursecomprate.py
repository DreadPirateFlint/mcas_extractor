from mcas_library import *


# initialize the extractor object
report = MCASExtract("https://profiles.doe.mass.edu/statereport/advcoursecomprate.aspx")

# set the output directory
output_directory = "outdir"

# display valid fields
print("getting fields for {}".format(report.get_url()))
report.print_report_options()
# quit()
# Set the parameters we'd like to loop over
request_params = dict()
request_params['ctl00$ContentPlaceHolder1$ddReportType'] = ['SCHOOL']
request_params['ctl00$ContentPlaceHolder1$ddYear'] = ['2018']
request_params['ctl00$ContentPlaceHolder1$ddSubgroup'] = ['5']

# used this to test for errors
# request_params['ctl00$ContentPlaceHolder1$ddSubGroup23'] = ['SHOOOT']

try:
    param2 = dict()
    for a in request_params['ctl00$ContentPlaceHolder1$ddReportType']:
        for b in request_params['ctl00$ContentPlaceHolder1$ddYear']:
            for e in request_params['ctl00$ContentPlaceHolder1$ddSubgroup']:
                param2['ctl00$ContentPlaceHolder1$ddReportType'] = a
                param2['ctl00$ContentPlaceHolder1$ddYear'] = b
                param2['ctl00$ContentPlaceHolder1$ddSubgroup'] = e
                report.get_report_real(parameters=param2)
                report.remove_header_row()
                # now add a year column
                report.add_column(0, 'Year', b)
                csvfilenamebase = "{}-{}-{}.csv".format(a, b, e)
                csvfilenamebase = os.path.join(output_directory, csvfilenamebase)
                report.write_csv(csvfilenamebase)
except MCASException as e:
    print("MCASExtract Error: {}".format(e))
    exit(-1)
