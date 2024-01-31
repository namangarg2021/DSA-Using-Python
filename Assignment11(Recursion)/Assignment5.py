# recursive function to print first n odd natural numbers in reverse Order

def print_first_odd_natural_numbers_in_reverse_order(n):
    if n <= 0:
        return
    print(2 * n - 1, end=" ")
    print_first_odd_natural_numbers_in_reverse_order(n - 1)


n = int(input("Enter the value of n:"))
print_first_odd_natural_numbers_in_reverse_order(n)
