my_list = [1, 2.5, "hello", 4, "world", 3.14]

int_list = []
float_list = []
str_list = []

for item in my_list:
    if isinstance(item, int):
        int_list.append(item)
    elif isinstance(item, float):
        float_list.append(item)
    elif isinstance(item, str):
        str_list.append(item)

print("Integers:", int_list)
print("Floats:", float_list)
print("Strings:", str_list)