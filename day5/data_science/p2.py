import matplotlib.pyplot as plt

# Sample data
a = [1, 2, 3, 4, 5]
b = [10, 20, 15, 30, 25]

# Create a new figure
plt.figure(figsize=(8, 5))

# Plot with line style, marker, color, and line width
plt.plot(a, b, color='green', marker='*',ms=90, linestyle='--', linewidth=2, label='Sales Data',mec='r')

# Labels and title
plt.xlabel("Days", fontsize=12)
plt.ylabel("Units Sold", fontsize=12)
plt.title("Sales Over Time", fontsize=14)

# Grid and legend
plt.grid(True)
plt.legend()

# Show plot
plt.show()
