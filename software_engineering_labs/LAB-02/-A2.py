import string

password = input()
upper_string = password.upper()
lower_string = password.lower()
list_of_errors = []

digit_flag = False
allowed_flag = True
special_character_flag = False
is_first_digit = False

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+-#"
special_characters = "+-#"

digit_flag = any(symbol.isdigit() for symbol in password)
allowed_flag = all(symbol in allowed for symbol in password)
for symbol in password:
    if symbol in set(special_characters):
        special_character_flag = True

if(password[0].isdigit()):
    is_first_digit = True

if len(password) < 8:
    list_of_errors.append("Длина пароля меньше 8")
if password == upper_string:
    list_of_errors.append("В пароле отсутствуют строчные буквы")
if password == lower_string:
    list_of_errors.append("В пароле отсутствуют заглавные буквы")
if digit_flag == False:
    list_of_errors.append("В пароле отсутствуют цифры")
if allowed_flag == False:
    list_of_errors.append("В пароле присутствуют непридусмотренные символы")
if special_character_flag == False:
    list_of_errors.append("В пароле отсутсвуют специальные символы")
if is_first_digit == True:
    list_of_errors.append("В пароле первый символ не должен быть цифрой")

if (len(list_of_errors) != 0):
    print(list_of_errors)
else:
    print("Пароль надежен")
