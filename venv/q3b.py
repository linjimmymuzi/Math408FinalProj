import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
import time

# Parameters
n = 100  # Number of trials
p = 0.8  # Probability of success
num_samples = 5000  # Number of Binomial random variables to generate

# Step 1: Precompute the CDF of the Binomial distribution
binom_cdf = np.cumsum([binom.pmf(k, n, p) for k in range(n + 1)])

# Step 2: Define a function to generate Binomial random variables using the inverse transformation method
def generate_binomial_inverse_transform(num_samples, binom_cdf):
    samples = []
    for _ in range(num_samples):
        # Generate a uniform random variable U ~ Uniform(0, 1)
        u = np.random.uniform(0, 1)
        # Step 3: Find the smallest k such that F(k) >= U
        k = np.searchsorted(binom_cdf, u)
        samples.append(k)
    return np.array(samples)

# Measure computation time
start_time = time.time()
binomial_samples = generate_binomial_inverse_transform(num_samples, binom_cdf)
end_time = time.time()

# Plot histogram of the generated samples
plt.hist(binomial_samples, bins=30, density=True, alpha=0.6, color='blue', label='Generated Samples')
plt.title("Histogram of Binomial Samples (Inverse Transform Method)")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Calculate empirical probability P(X <= 70)
empirical_prob_leq_70 = np.sum(binomial_samples <= 70) / num_samples

# Calculate theoretical probability P(X <= 70)
theoretical_prob_leq_70 = binom.cdf(70, n, p)

# Display results
print(f"Simulated P(X <= 70): {empirical_prob_leq_70:.6f}")
print(f"Theoretical P(X <= 70): {theoretical_prob_leq_70:.6f}")
print(f"Computation Time: {end_time - start_time:.4f} seconds")
