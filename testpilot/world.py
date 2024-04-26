def welcome():
    return "Hello, World!"

def fibonacci_of(n):
     if n in {0, 1}:  # Base case
         return n
     return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case


def calculate_mean(grades):
    return sum(grades) / len(grades)


def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None