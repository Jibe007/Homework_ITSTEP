#1.
userinput = str(input("Enter a text: "))

if userinput == userinput[::-1]:
    print("The input text is a palindrome")
else:
    print("The input text is not a palindrome")

#2.
user_input = str(input("Enter a text: "))

ascii_values = [ord(char) for char in user_input]

print("ASCII standard : ", ascii)



