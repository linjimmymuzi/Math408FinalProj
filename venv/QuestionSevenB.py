import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency


# Define a function to perform the mean and variance tests on z-scores
def test_normality(data, label, mean, std):
    # Transform to z-scores
    z_scores = (data - mean) / std

    # Test if mean of z-scores is 0 (z-test)
    z_mean = z_scores.mean()
    z_std = z_scores.std(ddof=1)
    n = len(z_scores)

    # Calculate z-statistic for the mean
    z_stat = (z_mean - 0) / (z_std / np.sqrt(n))  # Hypothesized mean is 0

    # Calculate test-statistic for the variance in chi-square
    sample_variance = np.var(z_scores, ddof=1)
    chi2_stat = (n - 1) * sample_variance / 1  # Hypothesized variance is 1

    # Print results
    print(n)
    print(f"Results for {label}:")
    print(f"Z Mean is {z_mean}")
    print(f"Z Std is {z_std}")
    print(f"DOF is {n-1}")
    print(f"Mean Test (z-test): z-statistic={z_stat}")
    print(f"Variance Test (Chi-Square): Chi2-statistic={chi2_stat}")
    print()


def test_independency(data_one, data_two):
    bins = [-np.inf, -0.01, 0.01, np.inf]  # Thresholds for categorization
    labels = ["Negative", "Neutral", "Positive"]

    one_binned = pd.cut(data_one, bins=bins, labels=labels)
    two_binned = pd.cut(data_two, bins=bins, labels=labels)

    # Create a contingency table
    contingency_table = pd.crosstab(one_binned, two_binned)

    # Perform the chi-square test of independence
    chi2_stat, p_value, dof, expected = chi2_contingency(contingency_table)

    # Output results
    print("Contingency Table:")
    print(contingency_table)
    print("\nChi-Square Test Results:")
    print(f"Chi-Square Statistic: {chi2_stat:.4f}")
    print(f"Degrees of Freedom: {dof}")
    print(f"p-value: {p_value:.4f}")
    print("\nExpected Frequencies:")
    print(expected)