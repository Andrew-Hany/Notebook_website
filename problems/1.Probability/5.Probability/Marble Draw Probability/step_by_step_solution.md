# Step-by-Step Solution for Marble Draw Probability

## Approach
1. **Understand the Problem:**
   - We need to simulate drawing a marble from a bag containing 3 red, 2 blue, and 1 green marble `n` times.
   - We need to calculate the probability of drawing a red marble.

2. **Plan the Solution:**
   - Initialize a counter for red marbles.
   - Loop `n` times to simulate each marble draw.
   - Use `random.choice` to simulate drawing a marble from the bag.
   - If the result is a red marble, increment the counter.
   - After the loop, calculate the probability by dividing the red marble count by `n`.

3. **Implement the Solution:**
   - Write the code to perform the above steps.

## Practical Example
- If we draw a marble 60 times, we expect around 30 draws to be a red marble.
- By simulating this process, we can estimate the probability of drawing a red marble.