# Step-by-Step Solution for Random Walk Probability

## Approach
1. **Understand the Problem:**
   - We need to simulate a random walk on a 2D grid starting from the origin (0, 0).
   - We need to simulate `n` steps, where each step is randomly chosen from the four possible directions: up, down, left, or right.
   - After `n` steps, we need to determine if the walker is back at the origin (0, 0).
   - We need to repeat this simulation for a specified number of trials to estimate the probability of the walker being at the origin after `n` steps.

2. **Plan the Solution:**
   - Initialize a counter for the number of times the walker returns to the origin.
   - Loop through the number of trials.
   - For each trial, initialize the walker's position at the origin (0, 0).
   - Loop through the number of steps.
   - Randomly choose a direction and update the walker's position accordingly.
   - After `n` steps, check if the walker is back at the origin.
   - If the walker is back at the origin, increment the counter.
   - After all trials, calculate the probability by dividing the counter by the number of trials.

3. **Implement the Solution:**
   - Write the code to perform the above steps.

## Practical Example
- If we simulate a random walk with 4 steps and 10000 trials, we expect the walker to return to the origin approximately 25% of the time.
- By simulating this process, we can estimate the probability of the walker being at the origin after `n` steps.