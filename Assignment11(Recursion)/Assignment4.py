# recursive function to print first n even natural numbers

def print_first_even_natural_numbers(n):
    if n <= 0:
        return
    print_first_even_natural_numbers(n - 1)
    print(2 * n, end=" ")


n = int(input("Enter the value of n:"))
print_first_even_natural_numbers(n)
