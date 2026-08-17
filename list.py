numbers = [12, 45, 7, 23, 45, 89, 12, 34, 5, 67]
# 1. Print all elements from the list.
print(numbers)

# 2. Print the first and last element.
print(numbers[0])
print(numbers[-1])

# 3. Find the total number of elements without manually counting them.
print(len(numbers))

# 4. Calculate the sum of all elements.
print(sum(numbers))

#5. Find the largest and smallest number.
print("Largest:",max(numbers))
print("smallest :",min(numbers))

# 6. Print all even numbers.
for num in numbers :
 if num % 2 == 0 :
   print(num)
# 7. Print all odd  numbers.
 for num in numbers:
   if num % 2 != 0:
     print(num)

# 8. Count how many even and odd numbers are present.

even = 0
odd = 0

for num in  numbers :
  if num % 2 == 0 :
    even += 1

else :
  odd +=1

print("Even numbers :",even)
print("odd numbers :, odd")

# 9. Check whether 23 exists in the list.

if 23 in numbers :
  print("23 exists in the list")

else :
  print("23 does not exist")

# 10. Find the index position of 89.
print(numbers.index(89))

# 11. Add 100 at the end of the list.
numbers.append(100)
print(numbers) 

# 12. Insert 50 at index position 3.
numbers. insert(3,50)

#13. Remove the first occurrence of 45.
numbers.remove(45)
print(numbers)
  