# Exact sampling distribution.........................................................................................................
# Expand a grid representing 5 8-sided dice. That is, create a DataFrame with five columns from a dictionary, named die1 to die5. 
# The rows should contain all possibilities for throwing five dice, each numbered 1 to 8.
# Expand a grid representing 5 8-sided dice
dice = expand_grid({
    'die1':[1,2,3,4,5,6,7,8],
    'die2':[1,2,3,4,5,6,7,8],
    'die3':[1,2,3,4,5,6,7,8],
    'die4':[1,2,3,4,5,6,7,8],
    'die5':[1,2,3,4,5,6,7,8]
})


# Print the result
print(dice)

# Add a column, mean_roll, to dice, that contains the mean of the five rolls as a categorical.
# Expand a grid representing 5 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = dice[['die1', 'die2', 'die3', 'die4', 'die5']].mean(axis=1) 
                     
                    
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Print result
print(dice)

# Create a bar plot of the mean_roll categorical column, so it displays the count of each mean_roll in increasing order from 1.0 to 8.0.
# Expand a grid representing 5 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] + 
                     dice['die3'] + dice['die4'] + 
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort=False).plot(kind='bar', rot=0)
plt.show()