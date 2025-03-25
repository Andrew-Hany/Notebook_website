# Step-by-Step Solution for Dice Roll Probability

## Approach
1. **Understand the Problem:**
   - We need to simulate rolling a fair six-sided die `n` times.
   - We need to calculate the probability of rolling a six.

2. **Plan the Solution:**
   - Initialize a counter for sixes.
   - Loop `n` times to simulate each die roll.
   - Use `random.randint(1, 6)` to simulate a fair die roll.
   - If the result is six, increment the counter.
   - After the loop, calculate the probability by dividing the six count by `n`.

3. **Implement the Solution:**
   - Write the code to perform the above steps.

## Practical Example
- If we roll a die 60 times, we expect around 10 rolls to be a six.
- By simulating this process, we can estimate the probability of rolling a six.