# recursive function to print sum of n natural numbers

def print_sum_natural_numbers(n):
    if n == 0:
        return 0
    return n + print_sum_natural_numbers(n - 1)


n = int(input("Enter the value of n:"))
print(print_sum_natural_numbers(n))
