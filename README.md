# mcas_extractor

This is the MCAS Extractor project, created for Boston Schools Fund 
by Kurt Overberg (kurt@xrtic.com) at Xrtic Consulting.

This tool allows the user to interact with the Massachusetts Comprehensive Assessment System.  The MCAS is a series 
of forms on websites that outputs data on Massachusetts schools.  This system is broken down into two parts:

1. The MCASExtractor class - Python container class used for accessing MCAS forms and the website.
2. The driver files - These are python scripts that roughly contain the information being requested from the 
MCAS site in question.  These driver scripts decide which parameters to request and how to process the output 
of the request.  Generally processing includes adding columns or deleting rows and writing out CSV files of the data.

