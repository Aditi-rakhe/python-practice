list2 = [10, 20, 30, [40, 50, [60, 80, 90], 100, 110, 120], [112, 114, 116], 221, 226, 336]
# 1. Access First-Level Elements
# print(list2[0])
# # What is the output of list2[0] and list2[3]?\
# list2[0]
# print(list2[3])
# # Extract the list [40, 50, [60, 80, 90], 100, 110, 120] using indexing.
# print(list2[3])
# Retrieve 60, 80, and 90 from the nested list using indexing.
# print(list2[3][2][0])
# print(list2[3][2][1])
# print(list2[3][2][2])
# # What is the output of list2[4][1]?
# print(list2[4][1])
# 6. Write a statement to access the element 336.
# print(list2[7])
# # 7. The last element (336).
# print(list2 [7])
# # 8. The second-to-last sub-list ([112, 114, 116]).
# print(list2[4])
# # 9.Access 110 from the sub-list [40, 50, [60, 80, 90], 100, 110, 120].
# print(list2[3][4])
# # 10. Retrieve the element 116 from the list [112, 114, 116].
# print(list2[4][2])
# 11. Extract 40 from [40, 50, [60, 80, 90], 100, 110, 120].
# print(list2[3][0])
# 12. Write a slice to extract [30, [40, 50, [60, 80, 90], 100, 110, 120]].
# print(list2[2:4])
#13. Extract [100, 110, 120] from the nested sub-list [40, 50, [60, 80, 90], 100, 110, 120].
# print(list2[3][3:6])
# 14.Write a slice to reverse the entire list2.
# print(list2[::-1])
# 15.Reverse the list [112, 114, 116].
# print(list2[4][::-1])
# 16.Write a slice to get [60, 80, 90].
# print(list2[3][2])
# 17.From the main list, extract [10, 30, [112, 114, 116]] using slicing.
# print(list2[0:5:2])
# 18.Slice to extract [221, 226, 336] from the main list.
# print(list2[5:8])
# 19.Write a slice to extract [40, 50, [60, 80, 90]].
# print(list2[3][0:3])
#20.Write a slice to get [10, 30, [112, 114, 116], 226].
# print([list2[0]]+ list2 [2:5])
# 21.How many elements are in list2[3] and list2[4]?
# print(len(list2[3]))
# print(len(list2[4]))
#22.Write the statement to extract [112, 114, 116] from list2.
# print(list2[4])
# Retrieve the element 80 from the third-level nested list [60, 80, 90].
# print(list2[3][2][1])
# # Access 110 using negative indexing.
# print(list2[-5][-2])
# 25.Extract the element 100 using a combination of indexes.
# print(list2[3][3])
# 26 Retrieve 90 from the list [60, 80, 90].
# print(list2[3][2][2])
# 27.Using negative indexing, extract 226 from list2.
# print(list2[-2])
# 28.What happens when you try list2[3][5][0]? Explain why.
# It gives a TypeError because list2[3][5] is 120, an integer, and integers cannot be indexed.
# 29.Retrieve the middle element 50 from [40, 50, [60, 80, 90], 100, 110, 120].
# print(list2[3][1])
# 30.Write statements to extract the first element (10) and the last element (336) of list2.
print(list2[0])
print(list2[-1])