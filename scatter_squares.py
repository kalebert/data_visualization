import matplotlib.pyplot as plt 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c="red", s=10)

# Below code charts graph with 
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axes. 
ax.axis([0, 1100, 0, 1100001])

plt.show()

# Use the below code to save graph to a file
# plt.savefig('squares_plot.png', bbox_inches='tight')