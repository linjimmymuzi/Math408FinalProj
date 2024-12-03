# Re-generate uniform random numbers
import numpy as np
import matplotlib.pyplot as plt
import QuestionOneC

# Probabilities and corresponding values
probabilities = [0.1, 0.2, 0.3, 0.4]
values = [15, 100, -100, 200]

# Generate 10,000 discrete random numbers based on the uniform random numbers
discrete_random_numbers = []
for u in QuestionOneC.built_in_random_numbers:  # Directly use the generated random numbers in question 1
    if u < 0.1:
        discrete_random_numbers.append(15)
    elif u < 0.3:
        discrete_random_numbers.append(100)
    elif u < 0.6:
        discrete_random_numbers.append(-100)
    else:
        discrete_random_numbers.append(200)

# Plot the histogram
plt.figure(figsize=(8, 6))
plt.hist(discrete_random_numbers, bins=[-150, 0, 50, 150, 250], edgecolor='black', rwidth=0.8)
plt.title("Histogram of Discrete Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.xticks(values)  # Ensure ticks match the discrete values
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()