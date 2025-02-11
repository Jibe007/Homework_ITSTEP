squared_numbers = {i**2 for i in range(1, 11)}
print("ricxvebi kvadratshi 1 dan 10 mde:", squared_numbers)

user_input = input("Sheiyvane sityva: ")
char_set = set(user_input)
print("Sityvis asoebi:", char_set) #es ar inaxavs tanmimdevrobas

tuple1 = (1, 2, 3, 4, 5, 6)
tuple2 = (4, 5, 5, 6, 6, 7)

combined_tuple = tuple(set(tuple1 + tuple2))
duplicated_values = []

for value in set(tuple1).intersection(tuple2):
    duplicated_values.append(value)

print("gaertianebuli tuple:", combined_tuple)
print("gaormagebuli valueebi:", duplicated_values)

input_tuple = (1, 2, 3, 4)
swapped_tuple = (input_tuple[-1], *input_tuple[1:-1], input_tuple[0])
print("tuple bolo da pirveli elementebis adgilis gacvlis shemdeg:", swapped_tuple)

nested_tuple = (1, (2, 3), (4, (5, 6)))
flattened_tuple = (nested_tuple[0], *nested_tuple[1], *nested_tuple[2][1])
print("chadgmuli tuple:", flattened_tuple)

set1 = {1, 2}
set2 = {'a', 'b'}
set_of_tuples = {(i, j) for i in set1 for j in set2}
print("tuples seti:", set_of_tuples)
