import numpy as np
import matplotlib.pyplot as plt

# Parameters
r = 0.05
sigma = 0.30
S0 = 95
n = 100

# Generate random variables from N(0, 2)
X = np.random.normal(0, np.sqrt(2), n)

# Recalculate Y with the factor of 2 applied to the term (r - sigma^2 / 2)
Y = S0 * np.exp(sigma * X + 2 * (r - (sigma**2) / 2))

# Recalculate the sample mean and standard deviation of Y
sample_mean_corrected_v2 = np.mean(Y)
sample_std_corrected_v2 = np.std(Y, ddof=1)

# Recalculate the 95% confidence interval
margin_of_error_corrected_v2 = z_critical * (sample_std_corrected_v2 / np.sqrt(n))
confidence_interval_corrected_v2 = (
    sample_mean_corrected_v2 - margin_of_error_corrected_v2,
    sample_mean_corrected_v2 + margin_of_error_corrected_v2,
)

# Plot the updated histogram of Y
plt.figure(figsize=(8, 6))
plt.hist(Y, bins=15, density=True, edgecolor="black", alpha=0.7, color="orange")
plt.title("Probability Histogram of Y (Corrected Formula with Time 2)")
plt.xlabel("Values of Y")
plt.ylabel("Probability Density")
plt.grid(alpha=0.6, linestyle="--")
plt.show()

# Display the updated results
sample_mean_corrected_v2, confidence_interval_corrected_v2