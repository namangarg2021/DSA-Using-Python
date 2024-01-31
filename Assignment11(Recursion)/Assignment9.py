# recursive function to print sum of n even natural numbers

def print_sum_even_natural_numbers(n):
    if n == 1:
        return 2
    return 2 * n + print_sum_even_natural_numbers(n - 1)


n = int(input("Enter the value of n:"))
print(print_sum_even_natural_numbers(n))
