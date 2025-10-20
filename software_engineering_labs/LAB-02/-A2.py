import string

password = input()
upper_string = password.upper()
lower_string = password.lower()

Digit_flag = False
Allowed_flag = False
special_character_flag = False

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+-#"
special_characters = "+-#"

Digit_flag = any(symbol.isdigit() for symbol in password)
Allowed_flag = all(symbol in allowed for symbol in password)
for symbol in password:
    if symbol in set(special_characters):
        special_character_flag = True

if len(password) != 8:
    print("Длина пароля не равна 8")
elif password == upper_string:
    print("В пароле отсутствуют строчные буквы")
elif password == lower_string:
    print("В пароле отсутствуют заглавные буквы")
elif Digit_flag == False:
    print("В пароле отсутствуют цифры")
elif Allowed_flag == False:
    print("В пароле присутствуют непридусмотренные символы")
elif special_character_flag == False:
    print("В пароле отсутствуют специальные символы")
else:
    print("Надежный пароль")


