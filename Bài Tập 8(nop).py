# 1.Write a Python function to find the maximum of three numbers.
def max_num(a,b,c):
    return max(a,b,c)
result=max_num(1,4,6)
print("Maximun of three numbers:",result)

# 2.Write a Python function to sum all the numbers in a list.
def sum_number(*args):
    return sum(args)
result=sum_number(1,3,4,7,8)
print("Sum:",result)

# 3.Write a Python program to reverse a string.
def reverse_str(s):
    return s[::-1]
result=reverse_str("Write a Python program to reverse a string")
print("Reverse a string:", result)

# 4.Write a Python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument.
def factorial(n):
    if n<0:
        return "Factorial is not define"
    elif n==0 or n==1:
        return 1
    else:
        result=1
        for i in range(1,n+1):
            result*=i
        return result
num=5
result=factorial(num)
print(f"Factorial of {num} is {result}")

# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
from math import sqrt
def is_prime(number:int) ->bool:
    if number<2:
        return False
    for i in range(2,int(sqrt(number))+1):
        if number%i==0:
            return False
    return True
print(is_prime(7))

# 6.Write a Python function to print
# 1.all prime numbers that less than a number (enter prompt keyboard).
def print_prime_under(n:int):
    for so in range(2,n):
        if is_prime(so):
            print(so,end=", ")
print_prime_under(10)
print()

# 2.the first N prime numbers.
def print_n_primes(n:int):
    so=2
    dem=0
    while dem<n:
        if is_prime(so):
            print(so, end=", ")
            dem+=1
        so+=1
print_n_primes(10)
# 7.Write a Python function to check whether a number is "Perfect" or not. Then print all perfect number that less than 1000.
def perfect_number(n:int):
    if n<2:
        return False
    sum=1
    for i in range(2,n//2+1):
        if n%i==0:
            sum+=i
    return sum==n
print(perfect_number(28))

def print_perfect_number_under(n:int):
     for so in range(2,n):
        if perfect_number(so):
             print(so,end=", ")
print_perfect_number_under(1000)


# 8.Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
import string
def is_pangram(s):
    alphabet=set(string.ascii_lowercase)
    return alphabet <= set(s.lower())
print(is_pangram("The quick brown fox jumps over the lazy dog"))