import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.05
sigma = 0.30
S0 = 95
n = 100

# Generate random variables from N(0, 2)
X = np.random.normal(0, np.sqrt(2), n)

# Calculate Y
Y = S0 * np.exp(sigma * X + 2 * (r - (sigma**2) / 2))

# Sample mean and standard deviation of Y
sample_mean = np.mean(Y)
sample_std = np.std(Y, ddof=1)  # ddof=1 for unbiased estimate, dof = n - ddof

# 95% confidence interval
z_critical = 1.96  # for 95% confidence level
margin_of_error = z_critical * (sample_std / np.sqrt(n))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

print(sample_mean, sample_std, confidence_interval)

# Plot the updated histogram of Y
plt.figure(figsize=(8, 6))
plt.hist(Y, bins=15, density=True, edgecolor="black", alpha=0.7, color="orange")
plt.title("Probability Histogram of Y")
plt.xlabel("Values of Y")
plt.ylabel("Probability Density")
plt.grid(alpha=0.6, linestyle="--")
plt.show()
