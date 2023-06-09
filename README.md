# AnoData
*Developer: **Edyta Pawlicka**   ed.pawlicka@gmail.com*

AnoData is a program designed to anonymize data from .csv files. It provides a user-friendly interface for selecting and 
modifying data columns, allowing you to generate anonymized versions of your data while preserving its structure and format.  
It can be particularly useful when working with client data and needing to prepare pre-defined visual analytics 
or demonstrate data structures without disclosing actual sensitive information.


**How program works:**
<br />⮩ Launch the AnoData program.
<br />⮩ Select the .csv file containing the data you want to anonymize (use sample 'csv_Superstore.csv' to test).
<br />⮩ The program will display a list of columns present in the selected file with fetched properties.
<br />⮩ For each column, specify the anonymization method and any required parameters.
<br />⮩ Click the bottom "Generate" button to start the anonymization process.
<br />⮩ AnoData will create a new anonymized .csv file with the modified data and save it in same location as your file.
<br />⮩ The program will display a success message once the anonymization is complete.


**Modules:**
<br />⮩ d_start_screen: gui of starting screen, initiating file selection
<br />⮩ e_gui: gui generated based on file selection (all columns and it's parameters), user set new properties 
<br />⮩ b_csv_entry: check correctness of csv file and describe its properties
<br />⮩ c_csv_process: process the data basing on user choices and generate new, anonymized csv

**Libraries:**
<br />⮩ csv
<br />⮩ tkinter
<br />⮩ datetime
<br />⮩ sys
<br />⮩ os
<br />⮩ random

**Ideas for the future:**
<br />⮩ other file types available (.hyper, .xlsx)
<br />⮩ protect user for entering wrong data type in second screen (Data Type - Ranges types match)
<br />⮩ program enhancement to analyze trends in given data, create data summary to use it before creating visual 
analytics (f.e. number of columns with particular datatype, number of rows, number of distinct values, are there nulls)
<br />⮩ automatic detection of delimiter type in csv