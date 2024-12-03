import numpy as np
import matplotlib.pyplot as plt

# Generate 10,000 uniformly distributed random numbers on [0, 1]
built_in_random_numbers = np.random.uniform(0, 1, 10000)

# Check mean and variance
built_in_mean = np.mean(built_in_random_numbers)
built_in_variance = np.var(built_in_random_numbers)

# Plot the histogram
plt.hist(built_in_random_numbers, bins=50, density=True, edgecolor='black')
plt.title('Histogram of Generated Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Display the results
print(built_in_mean, built_in_variance)