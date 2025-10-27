while True:
    try:
        height_of_the_rectangle = int(input("Введите высоту прямоугольника: "))
        width_of_the_rectangle = int(input("Введите ширину прямоугольника: "))
        break
    except ValueError:
        print("Ширина и высота - целые числа!")

for i in range(height_of_the_rectangle):
    print(width_of_the_rectangle * '#')

while True:
    try:
        height_of_the_triangle = int(input("Введите высоту треуголника: "))
        break
    except ValueError:
        print("Высота - целые числа!")


for i in range(height_of_the_triangle + 1):
    print(i * '#')


