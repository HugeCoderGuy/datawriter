# DataWriter 
This python package allows for added ease when saving data to a .csv for post processing later.  

Refer to example.py for a more thorough walkthrough
```python
from datawriter.datawriter import datawriter
writer_example = datawriter(filename="example", output_direct="deleteme", replace_file=True)
writer_example.write_header("col1", "col2", "col3")
for i in range(5):
    writer_example.write_row(i*.001, str(i), ["Hello World!"])
```
