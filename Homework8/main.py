def is_anagram(str1, str2):
    str1, str2 = str1.replace(" ", "").lower(), str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

word1 = input("Sheiyvane pirveli sityva: ")
word2 = input("Sheiyvane meore sityva: ")
if is_anagram(word1, word2):
    print(f"'{word1}' da '{word2}' anagramaa.")
else:
    print(f"'{word1}' da '{word2}' araa anagrama.")


def count_character_occurrences(string, char):
    return string.count(char)

input_string = input("Sheiyvane nebismieri sityva: ")
char_to_count = input("Romeli aso an komponenti davitvalo sityvis?: ")
count = count_character_occurrences(input_string, char_to_count)
print(f"The character '{char_to_count}' appears {count} times in the string.") #uketesi ver movufiqre

def fibonacci_sequence(n):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n_terms = int(input("Ramdeni fibonachis ricxvi ginda daibechdos?: "))
fib_sequence = fibonacci_sequence(n_terms)
print(f"pirveli {n_terms} fibonachis ricxvi aris: {fib_sequence}")
