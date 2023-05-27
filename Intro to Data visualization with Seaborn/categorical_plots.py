# countplots...............................................................................................
# Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
# Create count plot of internet usage
sns.catplot(kind="count", data= survey_data, x="Internet usage")


# Show plot
plt.show()

# Make the bars horizontal instead of vertical.
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Separate this plot into two side-by-side column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()
