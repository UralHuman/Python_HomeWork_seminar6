first_element = int(input("Введите первый элемент прогрессии: "))
difference = int(input("Введите разность: "))
number_elements = int(input("Введите колличество элементов: "))

list1 = []
n = first_element + (number_elements - 1) * difference
for i in range(number_elements):
    list1.append(n)
    n -= difference
list1.reverse()
print(list1)
