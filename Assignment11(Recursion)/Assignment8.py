# recursive function to print sum of n odd natural numbers

def print_sum_odd_natural_numbers(n):
    if n == 1:
        return 1
    return (2 * n - 1) + print_sum_odd_natural_numbers(n - 1)


n = int(input("Enter the value of n:"))
print(print_sum_odd_natural_numbers(n))
