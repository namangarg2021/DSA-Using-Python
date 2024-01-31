# recursive function to print first n even natural numbers in reverse Order

def print_first_even_natural_numbers_in_reverse_order(n):
    if n <= 0:
        return
    print(2 * n, " ")
    print_first_even_natural_numbers_in_reverse_order(n - 1)


n = int(input("Enter the value of n:"))
print_first_even_natural_numbers_in_reverse_order(n)
