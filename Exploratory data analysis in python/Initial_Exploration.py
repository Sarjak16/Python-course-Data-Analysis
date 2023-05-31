# .............................................................................Functions for initial exploration........................................................

# Use a pandas function to print the first five rows of the unemployment DataFrame.
# Print the first five rows of unemployment
print(unemployment.head())

# Use a pandas function to print a summary of column non-missing values and data types from the unemployment DataFrame.
# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print the summary statistics (count, mean, standard deviation, min, max, and quartile values) of each numerical column in unemployment.
# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())
