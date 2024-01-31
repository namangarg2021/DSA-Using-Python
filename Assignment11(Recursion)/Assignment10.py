# recursive function to find factorial of a number

def fact(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * fact(n - 1)


n = int(input("Enter the value of n:"))
print(fact(n))
