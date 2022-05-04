from mcas_library import *
from time import sleep

# initialize the extractor object
report = MCASExtract("https://profiles.doe.mass.edu/statereport/gradsattendingcollege.aspx")

# the prefix for this report
output_prefix = "IHE_ATTENDANCE_REPORT"

# set the output directory
output_directory = "outdir"
output_directory = os.path.join(output_directory, output_prefix)

# display valid fields
print("Requesting fields for URL: {}".format(report.get_url()))
report.print_report_options()
# quit()
# Set the parameters we'd like to loop over
request_params = dict()
request_params['ctl00$ContentPlaceHolder1$ddReportType'] = ['SCHOOL']
request_params['ctl00$ContentPlaceHolder1$ddYear'] = ['2018', '2017', '2016', '2015']
request_params['ctl00$ContentPlaceHolder1$ddInOutState'] = ['ALL', 'IN_STATE', 'OUT_OF_STATE']
request_params['ctl00$ContentPlaceHolder1$ddAttendRange'] = ['MARCH']
request_params['ctl00$ContentPlaceHolder1$ddPctDenomType'] = ['COLL_ATTEND']
request_params['ctl00$ContentPlaceHolder1$ddStudentGroup'] = ['ALL', 'LEP', 'ECODIS', 'HIGH', 'LOWINC', 'SPED', 'BL', 'AI', 'AS', 'HS', 'MR', 'HP', 'WH']

print("Requesting following parameters: ")
for req_param in request_params:
    print("request_params['{}'] = {}".format(req_param, request_params[req_param]))

try:
    param2 = dict()
    for a in request_params['ctl00$ContentPlaceHolder1$ddReportType']:
        for b in request_params['ctl00$ContentPlaceHolder1$ddYear']:
            for c in request_params['ctl00$ContentPlaceHolder1$ddInOutState']:
                for d in request_params['ctl00$ContentPlaceHolder1$ddAttendRange']:
                    for e in request_params['ctl00$ContentPlaceHolder1$ddPctDenomType']:
                        for f in request_params['ctl00$ContentPlaceHolder1$ddStudentGroup']:
                            param2['ctl00$ContentPlaceHolder1$ddReportType'] = a
                            param2['ctl00$ContentPlaceHolder1$ddYear'] = b
                            param2['ctl00$ContentPlaceHolder1$ddInOutState'] = c
                            param2['ctl00$ContentPlaceHolder1$ddAttendRange'] = d
                            param2['ctl00$ContentPlaceHolder1$ddPctDenomType'] = e
                            param2['ctl00$ContentPlaceHolder1$ddStudentGroup'] = f

                            sleep(0.5)

                            print("Requesting following parameters: ")
                            for req_param in param2:
                                print("request_params['{}'] = {}".format(req_param, param2[req_param]))

                            report.get_report_real(parameters=param2)
                            report.remove_header_row()
                                
                            # now add necessary columns
                            report.add_column(0, 'Year', b)
                            report.add_column(1, 'InOutState', c)
                            report.add_column(2, 'StudentGroup', f)

                            csvfilenamebase = "{}-{}-{}-{}-{}.csv".format(a, b, c, d, f)
                            csvfilenamebase = os.path.join(output_directory, a, csvfilenamebase)
                            report.write_csv(csvfilenamebase)
except MCASException as e:
    print("MCASExtract Error: {}".format(e))
    exit(-1)
