# Step-by-Step Solution for Coin Toss Probability

## Approach
1. **Understand the Problem:**
   - We need to simulate tossing a fair coin `n` times.
   - We need to calculate the probability of getting heads.

2. **Plan the Solution:**
   - Initialize a counter for heads.
   - Loop `n` times to simulate each coin toss.
   - Use `random.choice` to simulate a fair coin toss.
   - If the result is heads, increment the counter.
   - After the loop, calculate the probability by dividing the heads count by `n`.

3. **Implement the Solution:**
   - Write the code to perform the above steps.

## Practical Example
- If we toss a coin 100 times, we expect around 50 heads and 50 tails.
- By simulating this process, we can estimate the probability of getting heads.