import random

def right_solution(n):
    ace_count = 0
    for _ in range(n):
        if random.choice(['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']) == 'Ace':
            ace_count += 1
    return ace_count / n

def right_solution2(n):
    ace_count = 0
    for _ in range(n):
        if random.randint(1, 13) == 1:
            ace_count += 1
    return ace_count / n


# import your libraries here
import random

# Write your solution under solution(n):
# You can create as many functions as you want and call them inside solution(n):  
def solution(n):

    pass