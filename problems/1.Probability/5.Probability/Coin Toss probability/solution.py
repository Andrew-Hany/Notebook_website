import random

def right_solution(n):
    heads_count = 0
    for _ in range(n):
        if random.choice(['heads', 'tails']) == 'heads':
            heads_count += 1
    return heads_count / n


# import your libraries here
import random

# Write your solution under solution(n):
# You can create as many functions as you want and call them inside solution(n):  
def solution(n):

    pass
