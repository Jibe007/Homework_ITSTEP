#1.
number1 = int(input("number1: "))
number2 =  2
number3 = int(input("number3: "))

#print(number1 % number2)
print("number1 even",number1 % number2)
print("number3 odd",number3 % number2)

#2.

txt1 = "small big tall short middle top"
txt2 = "small"
txt3 = "tall"
txt4 = "middle"

print(txt2 in txt1)
print(txt3 in txt1)
print(txt4 in txt1)

if txt2 in txt1 :
    print("small")
if txt3 in txt1 :
    print("tall")
if txt4 in txt1 :
    print("middle")

txt5 = "big short top"
if txt2 and txt3 and txt4 not in txt5 :
    print("These three words were not found in the text")

#3.
number6 = int(input("number6: "))
number7 = int(input("number7: "))
print(number6+number7)
print(number6-number7)
print(number6/number7)
print(number6*number7)
print(number6**number7)
print(number6//number7)
print(number6%number7)




