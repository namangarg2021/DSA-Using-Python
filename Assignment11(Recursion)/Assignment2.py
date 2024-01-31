# recursive function to print first n natural numbers in reverse order

def print_first_natural_numbers_in_reverse_order(n):
    if n <= 0:
        return
    print(n, end=" ")
    print_first_natural_numbers_in_reverse_order(n - 1)


n = int(input("Enter the value of n:"))
print_first_natural_numbers_in_reverse_order(n)
