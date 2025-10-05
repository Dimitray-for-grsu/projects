import math

input_data = open("WCData1.txt", "r")

list_of_input_lines = [line.strip() for line in input_data]
number_of_lines_with_data = len(list_of_input_lines) - 2
list_of_temperatures = []
list_of_wind_speeds = []
list_of_WC_Effects= []
list_of_temperatures_with_WC_Effect = []
summ_of_adjusted_temperatures = 0

for i in range(0, number_of_lines_with_data):
    list_of_temperatures.append(float(list_of_input_lines[i + 2].split()[1]))
    list_of_wind_speeds.append(float(list_of_input_lines[i + 2].split()[2]))

for i in range(0, number_of_lines_with_data):
    list_of_temperatures_with_WC_Effect.append(round(35.74 + 0.6125 * list_of_temperatures[i] + (0.4275 * list_of_temperatures[i] - 35.75) * (list_of_wind_speeds[i] ** 0.16), 1))
    list_of_WC_Effects.append(math.ceil((list_of_temperatures_with_WC_Effect[i] - list_of_temperatures[i]) * 10) / 10)
    summ_of_adjusted_temperatures = summ_of_adjusted_temperatures + list_of_temperatures_with_WC_Effect[i]

average_adjusted_temperature = math.floor(summ_of_adjusted_temperatures / number_of_lines_with_data * 10) / 10

input_data.close()

output_data = open("WindChillReport1.txt", "x")
output_data.write("Time     WC temp     WC Effect \n")
output_data.write("------------------------------ \n")
for i in range(0, number_of_lines_with_data):
    output_data.write("{:12}{:5}{:12} \n".format(list_of_input_lines[i + 2].split()[0], list_of_temperatures_with_WC_Effect[i], list_of_WC_Effects[i]))
output_data.write("------------------------------ \n")
output_data.write("\n")
output_data.write("The average adjusted temperature, based on {} observations, was {}.\n".format(number_of_lines_with_data, average_adjusted_temperature))
output_data.close()