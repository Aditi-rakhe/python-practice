numbers = [12, 45, 7, 23, 45, 89, 12, 34, 5, 67]

# Different ways to print/access elements
# 1. Directly
# print(numbers)

# Using for loop
# for x in numbers :
#     print(x)

# # Using len() with index
# for i in range(len(numbers)):
#     print(numbers[i])

# Using * unpacking
# print(*numbers)

# # # using list
# print(list(numbers))

# # iter() and next() are used to get elements one by one from a list.
it = iter(numbers)

for x in numbers:
    print(next(it))


