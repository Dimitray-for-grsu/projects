text = input("Введите текст: \n")
abbreviation = []
output = ""

for i in range(0, len(text.split())):
    if len(text.split()[i]) > 2:
        abbreviation.append(text.split()[i][0].upper())

for i in range(0, len(abbreviation)):
    output += abbreviation[i]
print(output)
