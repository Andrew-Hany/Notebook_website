import random

def right_solution(input_list):
    steps, trials = input_list
    origin_count = 0
    for _ in range(trials):
        x, y = 0, 0
        for _ in range(steps):
            step = random.choice(['up', 'down', 'left', 'right'])
            if step == 'up':
                y += 1
            elif step == 'down':
                y -= 1
            elif step == 'left':
                x -= 1
            elif step == 'right':
                x += 1
        if x == 0 and y == 0:
            origin_count += 1
    return origin_count / trials


# import your libraries here
import random

# Write your solution under solution(n):
# You can create as many functions as you want and call them inside solution(n):  
def solution(input_list):
    steps, trials = input_list
    pass