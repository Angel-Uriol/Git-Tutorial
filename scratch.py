import random

def solution(password, key):
    table = {}
    counter = 0
    for i in key:
        first_value = ord('a') + counter
        table[first_value] = ord(i)
        counter+=1
    return password.translate(table)

def solution2(password, key):
    table = {ord('a') + i : ord(k) for i, k in enumerate(key)}
    return password.translate(table)


def generate_random_list(n):
    result = list(range(1, n + 1))  # Generate a list of numbers from 1 to n
    random.shuffle(result)  # Shuffle the list
    return result


print(generate_random_list(80))

