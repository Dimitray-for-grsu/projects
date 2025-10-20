import math
previous_value = int(input())
instant_value = int(input())
use_of_gas = instant_value - previous_value

if use_of_gas <= 300:
    cost = 21
if use_of_gas <=600:
    cost = 21 + 0.06 * (use_of_gas - 300)
if use_of_gas <=800:
    cost = 21 + 0.06 * 300 + 0.04 * (use_of_gas - 600)
if use_of_gas > 800:
    cost = 21 + 0.06 * 300 + 0.04 * 200 + 0.025 * (use_of_gas - 800)

average_cost = cost / (instant_value - previous_value)
average_cost = math.floor(average_cost * 100) / 100

print("{:17}{:14}{:18}{:15}{:14}".format("Предыдущие", "Текущие", "Использовано", "К оплате", "Ср.цена m^3"))
print("{:6}{:17}{:15}{:17}{:17}".format(previous_value, instant_value, use_of_gas, cost, average_cost))