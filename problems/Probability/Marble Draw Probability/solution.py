import random

def right_solution(n):
    red_count = 0
    for _ in range(n):
        if random.choice(['red', 'red', 'red', 'blue', 'blue', 'green']) == 'red':
            red_count += 1
    return red_count / n


# import your libraries here
import random

# Write your solution under solution(n):
# You can create as many functions as you want and call them inside solution(n):  
def solution(n):

    pass