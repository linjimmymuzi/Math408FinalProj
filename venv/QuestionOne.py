import numpy as np
import matplotlib.pyplot as plt

# Constants for the random number generator
a = 7**5
c = 0
m = 2**31 - 1
x0 = 1  # Initial value of x0 chosen randomly
n = 10000


# Random number generator function using the provided formula
def random_number_generator(a, c, m, x0, n):
    generated_numbers = []
    x = x0
    for _ in range(n):
        x = (a * x + c) % m
        generated_numbers.append(x/m)  # Scale to [0, 1]
    return generated_numbers


# Generate the numbers
random_numbers = random_number_generator(a, c, m, x0, n)

# Plot the histogram
plt.hist(random_numbers, bins=50, density=True, edgecolor='black')
plt.title('Histogram of Generated Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Calculate mean
sample_mean = sum(random_numbers) / len(random_numbers)

# Calculate sample variance
sample_variance = sum((x - sample_mean) ** 2 for x in random_numbers) / (len(random_numbers)-1)

# Calculate standard deviation
sample_sd = sample_variance**(1/2)

print("Mean:", sample_mean)
print("Variance:", sample_variance)
print("Standard Deviation", sample_sd)


# For Question e
# Generate pairs (u1, u2), (u2, u3), ..., (u9999, u10000)
pairs = [(random_numbers[i], random_numbers[i + 1]) for i in range(len(random_numbers) - 1)]

# Separate pairs into x and y
x_vals = [pair[0] for pair in pairs]
y_vals = [pair[1] for pair in pairs]

# Plot the pairs
plt.figure(figsize=(8, 8))
plt.scatter(x_vals, y_vals, s=1, alpha=0.5)
plt.title("Scatter Plot of Consecutive Pairs")
plt.xlabel("$u_n$")
plt.ylabel("$u_{n+1}$")
plt.grid(True)
plt.show()