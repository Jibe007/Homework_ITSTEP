
int_list = [10, 20, 30, 40]

def add_to_int_list(number):
    global int_list
    int_list.append(number)

num_to_add = int(input("ra ricxvi chavamato listshi: "))
add_to_int_list(num_to_add)
print("ganaxlebuli listi:", int_list)



def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return number % 10 + sum_of_digits(number // 10)

num = int(input("sheiyvane cifrebi gadabmulad da me shevkribav mat: "))
print("ricxvebis jami:", sum_of_digits(num))



def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

input_string = input("Sheiyvane nebismieri sityva shetrialebulad: ")
print("Shetrialebuli sityva:", reverse_string(input_string))



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n_terms = int(input("Ramdeni fibonachis ricxvi daibechdos?: "))
fib_sequence = [fibonacci(i) for i in range(n_terms)]
print(f"pirveli {n_terms} fibonachis ricxvebia:", fib_sequence)
