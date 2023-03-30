# list1 = []
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# list_index = []
# elem = 0


# while elem != 100:
#     elem = int(input(">>> "))
#     list1.append(elem)
#     if elem in list2:
#         ind = list1.index(elem)
#         list_index.append(ind)

# print(list_index)

# //////////////////////////////////////////////////////////////

list1 = []
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list_index = []
elem = 0

while elem != 100:
    elem = int(input(">>> "))
    list1.append(elem)
for i, elem2 in enumerate(list1):
    if elem2 in list2:
        list_index.append(i)

print(list_index)
