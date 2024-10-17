import pandas as pd
from io import StringIO

# Creating a string representation of the dataset 
string_data = """
Outlook Temperature Humidity Windy Play
overcast hot high FALSE yes
overcast cool normal TRUE yes
overcast mild high TRUE yes
overcast hot normal FALSE yes
rainy mild high FALSE yes
rainy cool normal FALSE yes
rainy cool normal TRUE no
rainy mild normal FALSE yes
rainy mild high TRUE no
sunny hot high FALSE no
sunny hot high TRUE no
sunny mild high FALSE no
sunny cool normal FALSE yes
sunny mild normal TRUE yes
"""

# Reading the dataset into a pandas DataFrame
data = StringIO(string_data)

# Loading the dataset into a pandas DataFrame
column_names = ["Outlook", "Temperature", "Humidity", "Windy", "Play"]
df = pd.read_csv(data, delim_whitespace=True, names=column_names, skiprows=1, dtype=str)

# Test 
print(df)
