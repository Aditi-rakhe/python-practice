# Find the second-largest number in a list
numbers = [10,20,25,8,9,20]

numbers.sort()

print(numbers[-2])

# Reverse list
num = [1,2,3,4,5]
print(num[::-1])

# Remove duplicates
num = [1,2,3,4,4,5,5,6,6]

print(list(set(num)))


#  Find largest from list
num= [10,20,30,40,50,15]
print(max(num))

# find smallest no.
num = [10,20,30,40,50]

print(min(num))

# vowels
text = "python"
print(sum(ch in "aeiou" for ch in text))

# palindrome

text = 'madam'

print(text == text[::-1])