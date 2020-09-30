import matplotlib.pyplot as plt 

from random_walk import RandomWalk 


# Make a random walk
rw = RandomWalk(500)
rw.fill_walk()

# Plot the points in the walk

plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=0.5) 

# Remove the axes
ax.get_xaxis().set_visible(False) 
ax.get_yaxis().set_visible(False)

plt.show()
