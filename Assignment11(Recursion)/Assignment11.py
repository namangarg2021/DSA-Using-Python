# recursive function to find sum of squares of first n natural numbers

def print_sum_square_natural_numbers(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return n * n + print_sum_square_natural_numbers(n - 1)


n = int(input("Enter the value of n:"))
print(print_sum_square_natural_numbers(n))
