import pandas as pd
import numpy as np
import timestring
from bokeh.charts import Histogram, show, output_file

# Load dataframe and perform operations with it.
df = pd.read_csv('bees_essential.csv')

# List of months by number.
# timestamps = [timestring.parse(row[2]) for row in df.itertuples()]
months = [timestring.parse(row[2])['month'] for row in df.itertuples()]
print(sorted(months))

# Define the plot
plot = Histogram(months, xlabel='Months', ylabel='Frequency', title='Bee/Wasp Complaints by Month in 2016')
handle = show(plot)  # Show the figure.

output_file('bees_histogram.html')