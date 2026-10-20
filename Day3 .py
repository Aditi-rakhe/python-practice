#  count  the number of element
num = [10,20,30,40,50,60]
print(len(num))

#  convert a string to uppercase 
text = "python programming"
print(text.upper())

# find common elements in two list
a = [1,2,3,4,5]
b=[3,4,5,6,2]
print(list(set(a)& set(b)))

#  square every no.
num = [1,2,3,4,5]
print([n**2 for  n in  num])

#  remove space from string
text = " python is    Sfun"
text = text .replace ("","")

print(text)