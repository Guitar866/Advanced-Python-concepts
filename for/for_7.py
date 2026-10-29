import math

n = int(input("Enter a number: "))
root = math.isqrt(n)

if root * root == n and root > 1:
    prime = True
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break

    if prime:
        print("Square root is prime")
    else:
        print("Square root is not prime")
else:
    print("Square root is not prime")
