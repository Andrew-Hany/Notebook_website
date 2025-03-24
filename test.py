import random
def solution(input_list):
    random.seed(42)
    steps, n= input_list
    count=0
    for i in range(n):
        start = (0,0)
        for j in range(steps):
            step = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
            start = (start[0] + step[0], start[1] + step[1])

        if start == (0,0):
            count+=1
    return count/n

import random

def right_solution(input_list):
    random.seed(42)
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
print(solution([10, 10000]) == right_solution([10, 10000]), solution([4, 10000]), right_solution([4, 10000]))