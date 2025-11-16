text = input("Введите текст: \n")
while text.find('(') != -1 and text.find(')') != -1:
    text = text.replace(text[text.find('('):text.find(')') + 1], '')
print(text)
