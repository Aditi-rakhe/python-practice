
# 1. Print the multiplication table of a number
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


#   2. Find the sum of numbers in a list without using sum()  
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total = total + num

print("Sum =", total)