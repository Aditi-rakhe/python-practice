numbers = [1, 2, 3, 2, 4, 3, 5]

duplicates = set()
print(duplicates)


num = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]

for i in num:
    if num.count(i) > 1:
        print(i)

