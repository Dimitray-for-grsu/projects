text = input("Введите текст: \n")
list_separatory_chars = []

for i in range(0, len(text)):
    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        list_separatory_chars.append(i)

for i in range(0, len(list_separatory_chars)):
    print(text[list_separatory_chars[i]:list_separatory_chars[i + 1]])
print(len(list_separatory_chars))
