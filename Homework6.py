# დავალება 1.

# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს წინადადება, 
# პროგრამას დააბეჭდინეთ დიქტის სახით რამდენჯერ არის თითოეული სიტყვა გამოყენებული წინადადებაში


# userinput= input("enter text: ") 
# words = userinput.lower().split()
# words_count = {}

# for word in words:
#     if word in words_count:
#           words_count[word] += 1
#     else:
#         words_count[word] = 1    

# print(words_count)



# დაწერეთ პითონის პროგრამა, რომელიც მომხმარებელს სთხოვს შეიყვანოს ორი რიცხვი და ერთი მათემატიკური ოპერატორი,
# ააწყვეთ კალკულატორი, რომელიც გამოთვლის შესაბამის მოქმედებას, 
# გამოიყენეთ დიქტები, სადაც key მნიშვნელობებად იქნება მათემატიკური ოპერატორები



# user_numb1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
# user_numb2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
# math_operator = input("შეიყვანეთ მათემატიკური ოპერატორი (+, -, *, /): ")

# operators = {'+', '-', '*', '/'}

# if math_operator in operators:
#     if math_operator == '+':
#         result = user_numb1 + user_numb2
   
#     elif math_operator == '-':
#         result = user_numb1 - user_numb2
   
#     elif math_operator == '*':
#         result = user_numb1 * user_numb2
   
#     elif math_operator == '/':
#         if user_numb2 != 0:
#             result = user_numb1 / user_numb2
#         else:
#             result = "არ შეიძლება 0-ზე გაყოფა"
# else:
#     result = "არასწორი ოპერატორი"

# print(result)
              


####დავალება 3.

# comperhension-ის გამოყენებით დააგენერირეთ დიქტი, 
# რომლის key მნიშვნელობები იქნება 1-დან 10-ის ჩათვლით რიცხვები,
# ხოლო value მათი კვადრატი



# num_dict = dict([(x, x**2) for x in range(1, 11)])
# print(num_dict)



#
#დავალება 4.  
#                     

# #შექმენით დიქტი, რომელიც ინახავს ინფორმაციას დეპარტამენტების და თანამშრომლების შესახებ, 
# თითოეულ თანამშრომელს უნდა ჰქონდეს ატრიბუტები: სახელი, გვარი, ასაკი, ხელფასი.
# გამოთვალეთ საშუალო ხელფასი დეპარტამენტების მიხედვით.


#                       ბევრი ვეწვალე და ვერაფრით მივხვდი როგორ მივწვდე სალარის, 
#                      key value  და key1 value1  ამ პრინციპითაც ვცადე მაგრამ არ გამომივიდა, ხუთშაბათს იქნებ გავიაროთ.
# 
# 
# 
# 
# departments = {
#     'HR': {
#         'employees': {
#             '1': {'first_name': 'ანა', 'last_name': 'მოლაშვილი', 'age': 29, 'salary': 2600},
#             '2': {'first_name': 'ქეთევანი', 'last_name': 'გელაშვილი', 'age': 28, 'salary': 3600}
#         }
#     },
#     'IT': {
#         'employees': [
#             {'first_name': 'ალექსანდრე', 'last_name': 'ამაშუკელი', 'age': 26, 'salary': 3200},
#             {'first_name': 'დავით', 'last_name': 'ჩოხელი', 'age': 27, 'salary': 3400}
#         ]
#     },
#     'marketing': {
#         'employees': [
#             {'first_name': 'ნიკოლოზ', 'last_name': 'დევდარიანი', 'age': 29, 'salary': 4850},
#             {'first_name': 'ანა', 'last_name': 'მაისურაძე', 'age': 26, 'salary': 4700}
#         ]
#     }
# }



