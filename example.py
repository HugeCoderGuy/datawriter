from datawriter.datawriter import datawriter

'''
Defaults of datawriter include:
DataWriter(filename='dataLog', output_direct='Data', replace_file=False, timestamp=True, \
            silent=False, txtmode=False)
            
After instantiating a class instance, you can call the .write_header or .write_row methods
to create the columns. Note that write header can be called with a single list input or
various *arg inputs.
'''
# Initialize instrument and datawriter
writer_example = datawriter(filename="example", output_direct="deleteme", replace_file=True)

# identify the indexes of your columns of data that you want to collect
writer_example.write_header("col1", "col2", "col3")

# for in in data collected, write to .csv or .txt. Note that the file will not be corrupted 
# even if your script errors out midway.
for i in range(5):
    writer_example.write_row(i*.001, str(i), ["Hello World!"])
    
# final example to show list input
data = [222.113451, "data", 12334556568767.342435465765765754]
writer_example.write_row(data)