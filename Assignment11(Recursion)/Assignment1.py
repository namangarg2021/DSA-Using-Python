# recursive function to print first n natural numbers

def print_first_natural_numbers(n):
    if n <= 0:
        return
    print_first_natural_numbers(n - 1)
    print(n, end=" ")


n = int(input("Enter the value of n:"))
print_first_natural_numbers(n)
