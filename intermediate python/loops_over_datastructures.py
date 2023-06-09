# Write a for loop that iterates over the rows of cars and on each iteration
# perform two print() calls: one to print out the row label and one to print out all of the rows contents.
#solution:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
    
# Using the iterators lab and row, adapt the code in the for loop such that the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
# The output should be in the form "country: cars_per_cap". Make sure to print out this exact string (with the correct spacing).
# You can use str() to convert your integer data to a string so that you can print it in conjunction with the country label.
#solution:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+": "+str(row["cars_per_cap"]))

#     Use a for loop to add a new column, named COUNTRY, that contains a uppercase version of the country names in the "country" column. 
# You can use the string method upper() for this.
# To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.
#solution:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, rows in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = rows["country"].upper()


# Print cars
print(cars)
