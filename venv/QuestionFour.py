import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate 100 random variables from N(0, 3)
n = 100
mean = 0
std_dev = np.sqrt(3)
random_variables = np.random.normal(mean, std_dev, n)

# Calculate E(X^2 + 2cos(X)) for each sample
sample_values = random_variables**2 + 2 * np.cos(random_variables)
sample_mean = np.mean(sample_values)
sample_std = np.std(sample_values, ddof=1)  # ddof=1 for unbiased estimate, dof = n - ddof

# Calculate the 95% confidence interval
z_critical = 1.96  # For 95% confidence level
margin_of_error = z_critical * (sample_std / np.sqrt(n))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(sample_mean, sample_std, confidence_interval)

# Plot the histogram
plt.figure(figsize=(8, 6))
plt.hist(sample_values, bins=15, density=True, edgecolor="black", alpha=0.7)
plt.title("Probability Histogram of Sample Means")
plt.xlabel("Values of $X^2 + 2cos(X)$")
plt.ylabel("Probability Density")
plt.grid(alpha=0.6, linestyle='--')
plt.show()