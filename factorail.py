
import math
def factorial(n):
    product = 1 
    for i in range(1,n+1): 
        product *= i
    return product
n = int(input("Enter n: "))
if n < 0:
    print("n must be a non-negative integer")
else:
    product = factorial(n)
    print(product)
print(math.factorial(5))