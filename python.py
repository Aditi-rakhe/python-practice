# # Write a function to print "Hello, World!".
# def hello():
#     print("hello world!")
# hello()

# Write a function that takes two numbers as arguments and returns their sum.
# def sum():

#     a= 10
#     b= 20
  
#     print(a+b)
# sum()
# Write a function to check whether a number is even or odd.

# def  check_even_odd(n):
#     if n%2==0:
#         print("Even")
#     else:
#         print("odd")
# check_even_odd(10)

# Write a function to find the largest of two numbers without using max().

# def largest_two_num(a,b):
   
#     if a > b:
#         print(a)
#     else:
#         print(b)
# largest_two_num(10,20)

# Write a function to calculate the factorial of a number.
# def factorial(n):
#     fact = 1

#     for i in range(1, n + 1):
#         fact = fact * i

#     return fact

# print(factorial(5))

# Write a function to c(heck whether a number is prime or no

# def prime(n):
#   for i in range (2,n):
#     if n % i == 0:
#       print("not prime")
#       return
#     print("prime")

# prime(25)
# Write a function to reverse a number.

def reverse(n):
  rev= 0

  while n > 0:
    digit = n % 10
    rev= rev*10 + digit
    n = n//10

  return rev

print(reverse(1234))

def reverse(n):
  rev= 0

  while n > 0:
    digit = n % 10
    rev= rev*10 + digit
    n = n//10

    return rev

print(reverse(1234))

# Write a function to check whether a number is a palindrome.

def palindrome(n):
  original = n

  while n >0:
    digit = n % 10
    rev = rev*10 +digit
    n = n//10

  return rev
print(121)
    