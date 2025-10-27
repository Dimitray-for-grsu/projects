packets = input("Введите данные: ")

if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")

number_of_packets = len(packets)
number_of_loosing_packets = packets.count('0')
temp_number_of_loosing_packets = 0
list_of_loosing_sequences = []
percentage_of_loosing_packets = round(number_of_loosing_packets / number_of_packets * 100, 1)

for packet in packets:
    if packet == '0':
        temp_number_of_loosing_packets = temp_number_of_loosing_packets + 1
    else:
        list_of_loosing_sequences.append(temp_number_of_loosing_packets)
        temp_number_of_loosing_packets = 0

biggest_loosing_sequence = max(list_of_loosing_sequences)

print("Общее колличество пакетов: ", number_of_packets)
print("Общее колличество потерянных пакетов: ", number_of_loosing_packets)
print("Длинна самой длинной последовательности потерянных пакетов: " ,biggest_loosing_sequence)
print("Процент потерь: ", percentage_of_loosing_packets, "%")
if 0 <= percentage_of_loosing_packets < 1:
    print("Качество сети отличное")
elif 1 <= percentage_of_loosing_packets < 5:
    print("Качество сети хорошее")
elif 5 <= percentage_of_loosing_packets < 10:
    print("Качество сети удовлетворительное")
elif 10 <= percentage_of_loosing_packets < 20:
    print("Качество сети плохое")
elif percentage_of_loosing_packets > 20:
    print("Критическое сосотояние сети")
