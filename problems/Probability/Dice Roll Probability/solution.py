import random

def right_solution(n):
    six_count = 0
    for _ in range(n):
        if random.randint(1, 6) == 6:
            six_count += 1
    return six_count / n


# import your libraries here
import random

# Write your solution under solution(n):
# You can create as many functions as you want and call them inside solution(n):  
def solution(n):

    pass