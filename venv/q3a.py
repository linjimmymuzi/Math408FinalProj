import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.stats import binom

# Part (a): Generate Bernoulli random variables and add results
n = 100  # number of trials
p = 0.8  # probability of success
num_samples = 5000

# Start timing for method (a)
start_a = time.time()
bernoulli_samples = np.random.binomial(1, p, (num_samples, n))
binomial_from_bernoulli = bernoulli_samples.sum(axis=1)
end_a = time.time()

# Calculate the probability of Binomial random variable <= 70
prob_a = np.mean(binomial_from_bernoulli <= 70)

# Theoretical probability using binomial CDF
theoretical_prob = binom.cdf(70, n, p)

# Plot histogram for method (a)
plt.hist(binomial_from_bernoulli, bins=30, density=True, alpha=0.6, color='blue')
plt.title('Histogram of Binomial Distribution (Generated from Bernoulli RVs)')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()

# Display results
time_a = end_a - start_a

print("Results:")
print(f"Probability (Method a): {prob_a}")
print(f"Theoretical Probability: {theoretical_prob}")
print(f"Time (Method a): {time_a:.4f} seconds")
