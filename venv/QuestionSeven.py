import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm, shapiro, kstest
from QuestionSevenB import test_normality

# Fetch daily price data for Apple (AAPL) and Tesla (TSLA) for the past year
start_date = "2023-12-01"
end_date = "2024-12-01"
aapl_data = yf.download("AAPL", start=start_date, end=end_date)
tsla_data = yf.download("TSLA", start=start_date, end=end_date)

# Calculate daily returns
aapl_data['Daily Return'] = aapl_data['Adj Close'] - aapl_data['Adj Close'].shift(1)
tsla_data['Daily Return'] = tsla_data['Adj Close'] - tsla_data['Adj Close'].shift(1)

# Drop NaN values created by the shift operation
aapl_returns = aapl_data['Daily Return'].dropna()
tsla_returns = tsla_data['Daily Return'].dropna()

print(len(aapl_returns))
print(len(tsla_returns))

# Summarize results
print("Summary of Apple Returns:")
print(aapl_returns.describe())
print("\nSummary of Tesla Returns:")
print(tsla_returns.describe())

# Plot histograms and superimpose fitted normal densities
for returns, label in zip([aapl_returns, tsla_returns], ['Apple', 'Tesla']):
    mean, std = returns.mean(), returns.std()
    x = np.linspace(returns.min(), returns.max(), 100)
    pdf = norm.pdf(x, mean, std)

    plt.figure(figsize=(8, 6))
    plt.hist(returns, bins=30, density=True, alpha=0.6, edgecolor="black")
    plt.plot(x, pdf, "r-", lw=2, label=f"Fitted Normal Density\nMean={mean:.4f}, Std={std:.4f}")
    plt.title(f"{label} Daily Returns with Normal")
    plt.xlabel("Daily Returns (Actual)")
    plt.ylabel("Probability Density")
    plt.legend()
    plt.grid(alpha=0.5)
    plt.show()

    test_normality(returns, label, mean, std)

# Perform Shapiro-Wilk Test for normality
print("Shapiro-Wilk Test Results for Normality:")
apple_shapiro = shapiro(aapl_returns)
tesla_shapiro = shapiro(tsla_returns)
print(f"Apple: Statistic={apple_shapiro.statistic}, p-value={apple_shapiro.pvalue}")
print(f"Tesla: Statistic={tesla_shapiro.statistic}, p-value={tesla_shapiro.pvalue}")