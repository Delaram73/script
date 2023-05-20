import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a figure and plot the data
fig, ax = plt.subplots()
ax.plot(x, y)

# Add labels and title
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_title('Sine Wave')

# Display the figure
plt.show()
