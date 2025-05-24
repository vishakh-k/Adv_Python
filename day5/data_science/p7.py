import matplotlib.pyplot as plt

# Data for three equal segments
sizes = [1, 1, 1]
colors = ['white', 'black', 'white']

# Create figure and axis
fig, ax = plt.subplots()

# Plot pie chart with wedge properties for border line
ax.pie(
    sizes,
    colors=colors,
    startangle=90,  # Rotate to point upward
    wedgeprops={'edgecolor': 'black', 'linewidth': 2}
)

# Draw circle around to simulate outer boundary
centre_circle = plt.Circle((0, 0), 0.70, color='black', fill=False, linewidth=3)
ax.add_artist(centre_circle)

# Equal aspect ratio ensures the pie is drawn as a circle.
ax.axis('equal')

plt.title("Mercedes-Benz Style Pie")
plt.show()
