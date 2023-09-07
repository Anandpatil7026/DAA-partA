my_array = []
for i in range(5):
    num = int(input(f"Enter integer {i + 1}: "))
    my_array.append(num)
print("Array items:")
for item in my_array:
    print(item)
index=int(input(f"enter index number:"))
print(my_array[index-1])
