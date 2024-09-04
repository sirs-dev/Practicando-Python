## 04_higher_order_functions.py ##
def sum_one(value):
    return value + 1


def sum_two_values(first_value, second_value):
    return sum_one(first_value + second_value)

print(sum_two_values(8, 2))
