import random
import time

all_spending_time = 0
number_of_tasks = int(input("Введите колличество примеров: "))
right_answers = number_of_tasks

for i in range(number_of_tasks):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    start_time = time.time()
    print(f"Вопрос {i + 1}/{number_of_tasks}: ")
    while True:
        try:
            answer = int(input(f"{a} × {b} = "))
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")


    time_spend = time.time() - start_time
    if (answer == a * b):
        all_spending_time = all_spending_time + time_spend
        print(f"Верно! (Затраченное время: {round(time_spend, 1)})")
    else:
        right_answers = right_answers - 1
        print("Неверно!")

print(33 * "=")
print("СТАТИСТИКА:")
print(33 * "=")
print(f"Общее время: {round(all_spending_time, 1)} секунд")
print(f"Среднее затраченное время: {round(all_spending_time / number_of_tasks), 1} сек")
print(f"Правильных ответов: {right_answers}/{number_of_tasks}")
print(f"Процент правильных: {round(right_answers / number_of_tasks * 100, 2)}%")

