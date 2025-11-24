import numpy as np

# 1. Create 2D array for 4 branches over 6 months
transactions = np.array([
    [1200, 1500, 1600, 1700, 1800, 2000],  # Branch 1
    [1300, 1400, 1500, 1600, 1650, 1750],  # Branch 2
    [1100, 1200, 1250, 1300, 1400, 1500],  # Branch 3
    [2000, 2100, 2200, 2300, 2400, 2500]   # Branch 4
])

print("Transaction Array:\n", transactions)

# 2. Total transactions per branch
total_per_branch = np.sum(transactions, axis=1)
print("\nTotal transactions per branch:", total_per_branch)

# 3. Branch with highest total
highest_branch = np.argmax(total_per_branch) + 1
print("\nBranch with highest total transactions: Branch", highest_branch)

# 4. Average monthly transaction across all branches
avg_monthly = np.mean(transactions)
print("\nAverage monthly transaction volume:", avg_monthly)

# 5. Reshape to 3x8
reshaped = transactions.reshape(3, 8)
print("\nReshaped Array (3x8):\n", reshaped)

print("\nImplication: Reshaping changes how data is organized but NOT the data values.")
