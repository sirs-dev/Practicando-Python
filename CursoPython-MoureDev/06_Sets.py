### Sets ###

my_set = set()
my_other_set = {}

my_other_set = {"Sergio", "Ruiz", 1.81, 26}
my_other_set.add("Santiago")
my_other_set.add("Ruiz")
my_set.add("Daniel")
print(my_other_set.union(my_set))
print(len(my_other_set))
print(my_other_set)
print("Sergio" in my_other_set)
print("Juan" in my_other_set)
print(my_set)

