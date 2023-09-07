# using inbuilt function

import math

def gcd(a, b):
    return math.gcd(a, b)

num1 = int(input("Enter first num: "))
num2 = int(input("Enter secoond num: "))
result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", result)


# using while loop

a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
 
divisor = min(a, b)
 
while divisor > 0:
    if a%divisor == 0 and b%divisor == 0:
        print('The GCD is', divisor)
        break
    divisor -= 1


# using recursion (Euclidian Algorithm)

def eGCD(a, b):
    if b == 0:
        return a
    else:
        return eGCD(b, a%b)
    
a = int(input("Enter 1st num: "))
b = int(input("Enter 2nd num: "))
result = eGCD(a, b)
print('The GCD is', result)
