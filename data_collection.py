import pandas as pd
import numpy as np
#Open file
my_file=pd.read_csv('example_data.txt', sep=" ")
file=pd.DataFrame(my_file)

#Now I am creating a new csv with data to be fetched into the table.
#table=pd.open_csv('table')
