import pandas as pd
import numpy as np
import ast
import math
import matplotlib.pyplot as plt


# Load the CSV file
input_file = '/home/przhan/MTE544_student/Raw Data/laser_content_line.csv'  # Replace with your CSV file path
output_file = 'cleaned_output.csv'

#Define a custom function to parse the array from string format (if it's a stringified array)
def parse_array(array_str):
    try:
        return ast.literal_eval(array_str)  # Safely evaluate the string to a Python object
    except (SyntaxError, ValueError):
        print(f"Error parsing array: {array_str}")
        return None

# Function to clean data
def clean_data(value):
    if isinstance(value, str):  # Check if the value is a string
        # Remove brackets and leading/trailing spaces
        return value.replace('[', '').replace('])', '').strip()
    return value  # Return the value unchanged if it's not a string


# Read the second row only (skip the first row with headers)
df = pd.read_csv(input_file, skiprows=1, nrows=1, header=None)

# Parse the first column which contains the array-like data
df[0] = df[0].apply(parse_array)

# Get the second line (which is now the only line in df after skipping the header)
second_line = df.iloc[0]

# Convert the second line to a DataFrame to write it easily to a CSV
df_second_line = pd.DataFrame([second_line])

# Write the second line to a new CSV file
df_second_line.to_csv('temp_file.csv', index=False, header=False)

# Apply the clean_data function to all cells in the DataFrame
df_cleaned = df_second_line.map(clean_data)

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv(output_file, index=False, header=False)  # Replace 'cleaned_output.csv' with your desired output file path

#print(df_cleaned)

cleaned_df = pd.read_csv(output_file, header = None)
#print(cleaned_df.shape)
#Angle increment
angle_increment = df.iloc[0, -3]  # 0 for the first row, -2 for the second last column

print(angle_increment)

angle = 0
x_cart = []
y_cart = []

# print("angle increment" + angle_increment + '\n')

#Extracted one single line of the CSV up to this point. Now we filter for inf and NaN

for readings in (cleaned_df-2): #take out last 2, since those are angle increment and timestamps
    #Take the angle, then multiply by sin and cos to get x and y, then convert            
            if (math.isinf(readings) == False and math.isnan(readings) == False):
            #if (range > range_min) and (range < range_max)
                x_cart.append(math.cos(angle)*readings)
                y_cart.append(math.sin(angle)*readings)
            angle += angle_increment

print(x_cart + y_cart)

#plotting x_cart vs y_cart
plt.scatter(x_cart, y_cart)
plt.legend()
plt.grid()
plt.show()