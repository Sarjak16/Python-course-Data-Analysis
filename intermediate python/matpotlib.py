# #LINE PLOT..............................................................................................................................................................
# print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. Use two print() functions.
# Before you can start, you should import matplotlib.pyplot as plt. pyplot is a sub-package of matplotlib, hence the dot.
# Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. Don't forget to finish off with the plt.show() function to actually display the plot.

#solution:
# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year,pop)

# Display the plot with plt.show()
plt.show()

#EX 2
# Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
# Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
# Don't forget to finish off with a plt.show() command, to actually display the plot.

#SOLUTION:
# Print the last item of gdp_cap and life_exp
print(gdp_cap[-1])
print(life_exp[-1])

# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis
plt.plot(gdp_cap, life_exp)

# Display the plot
plt.show()

# Scatterplot..............................................................................................................................
# Change the line plot that's coded in the script to a scatter plot.
# A correlation will become clear when you display the GDP per capita on a logarithmic scale. Add the line plt.xscale('log').
# Finish off your script with plt.show() to display the plot.

#Solution:
# Change the line plot below to a scatter plot
plt.scatter(gdp_cap, life_exp)

# Put the x-axis on a logarithmic scale
plt.xscale('log')

# Show plot
plt.show()

#ex 2:
# Start from scratch: import matplotlib.pyplot as plt.
# Build a scatter plot, where pop is mapped on the horizontal axis, and life_exp is mapped on the vertical axis.
# Finish the script with plt.show() to actually display the plot. Do you see a correlation?
#Solution:

# Import package

import matplotlib.pyplot as plt
# Build Scatter plot
plt.scatter(pop,life_exp)

# Show plot
plt.show()

#HISTOGRAM........................................................................................................................................................
# Use plt.hist() to create a histogram of the values in life_exp. Do not specify the number of bins; Python will set the number of bins to 10 by default for you.
# Add plt.show() to actually display the histogram. Can you tell which bin contains the most observations?
#SOLUTION:
# Create histogram of life_exp data
plt.hist(life_exp)

# Display histogram
plt.show()

#Build a histogram (2): bins
# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clear plot again
plt.show()
plt.clf()


#ex 2:
#Build a histogram (2): bins
# Build histogram with 5 bins
plt.hist(life_exp, bins = 5)

# Show and clear plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp, bins = 20)

# Show and clear plot again
plt.show()
plt.clf()

#ex3:
# Build a histogram of life_exp with 15 bins.
# Build a histogram of life_exp1950, also with 15 bins. Is there a big difference with the histogram for the 2007 data?

# Histogram of life_exp, 15 bins
plt.hist(life_exp,15)

# Show and clear plot
plt.show()
plt.clf()

# Histogram of life_exp1950, 15 bins
plt.hist(life_exp1950,15)

# Show and clear plot again
plt.show()
plt.clf


















