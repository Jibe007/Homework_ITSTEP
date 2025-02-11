from functools import reduce


def zip_lists(list1, list2):
    return [f"({x}, '{y}')" for x, y in zip(list1, list2)]


even_elements = lambda lst: [x for x in lst if x % 2 == 0]

positive_values = lambda lst: filter(lambda x: x > 0, lst)

palindrome_check = lambda lst: filter(lambda s: s == s[::-1], lst)


def product_of_elements(lst):
    if not all(isinstance(x, (int, float)) for x in lst):
        raise TypeError("Yvela wevri unda iyos ricxvi!")
    return reduce(lambda x, y: x * y, lst)


def filter_by_ending(strings, ending):
    return list(filter(lambda x: x.endswith(ending), strings))


# Magalitebi

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(zip_lists(list1, list2))

print("---------")

list_nums = [1, 2, 3, 4, 5, 6, 7]
print(even_elements(list_nums))

print("---------")

numbers = [-5, -3, 0, 1, 2, 4]
print(list(positive_values(numbers)))

print("---------")

strings = ['level', 'world', 'madam', 'python']
print(list(palindrome_check(strings)))

print("---------")

nums = [1, 2, 3, 4, 5]
print(product_of_elements(nums))

print("---------")

words = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
print(filter_by_ending(words, ending))
