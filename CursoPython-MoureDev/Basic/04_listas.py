### List ### 

my_list = list()
my_other_list = []


my_list = [25, 23, 54, 12]

print(len(my_list))
print(my_list[1])
print(my_list[-1])

new_list = ["Sergio", 26, 1.26]
print(new_list)
print(my_list + new_list)

nombre, edad, altura = new_list
new_list.append("Santiago")
new_list.insert(1, "Ruiz")
print(new_list)
new_list.remove("Ruiz")
print(new_list)
new_list.pop()
print(new_list)
new_list.pop(0)
print(new_list)
new_list.clear()
print(new_list)

new_list = my_list.copy()
print(new_list)
print(new_list[0:2])
