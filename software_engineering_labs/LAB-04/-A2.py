text = input("Введите текст: \n")
list_separatory_chars = []

for i in range(0, len(text)):
    if text[i] == '.' or text[i] == '!' or text[i] == '?':
        list_separatory_chars.append(i)

print(text[0:list_separatory_chars[0]] + text[list_separatory_chars[0]])
for i in range(0, len(list_separatory_chars) - 1):
    print((text[(list_separatory_chars[i] + 1):list_separatory_chars[i + 1]] + text[list_separatory_chars[i + 1]]).strip())
print("Колличество предложений: ", len(list_separatory_chars))
