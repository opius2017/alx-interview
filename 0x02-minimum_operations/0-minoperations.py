#!/usr/bin/python3

def minOperations(n):
    # If n is less than 2, it's impossible to achieve.
    if n < 2:
        return 0

    # Initialize an array to store the minimum number of operations needed for each position.
    dp = [0] * (n + 1)

    # Loop through each position from 2 to n.
    for i in range(2, n + 1):
        dp[i] = i  # Initialize with the maximum possible operations.
        for j in range(2, i):
            if i % j == 0:
                # If i is divisible by j, it means we can copy j characters and paste (i // j - 1) times.
                dp[i] = min(dp[i], dp[j] + (i // j))

    return dp[n]

# Example usage:
n = 9
result = minOperations(n)
print("Number of operations:", result)
