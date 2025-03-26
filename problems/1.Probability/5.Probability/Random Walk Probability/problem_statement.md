# Random Walk Probability

## Description
Write a function that simulates a random walk on a 2D grid starting from the origin (0, 0). The function should simulate `n` steps, where each step is randomly chosen from the four possible directions: up, down, left, or right. After `n` steps, the function should determine if the walker is back at the origin (0, 0). The function should repeat this simulation for a specified number of trials to estimate the probability of the walker being at the origin after `n` steps. The function should return this estimated probability.

## Test Cases
- **Input:** [4, 10000]
  **Expected Output:** 0.25
- **Input:** [100, 10000]
  **Expected Output:** 0.1