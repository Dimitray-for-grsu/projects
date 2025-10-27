def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        print(columns * ch)

def draw_triangle(rows, ch):
    for i in range(rows + 1):
        print(i * ch)

def draw_frame(rows, columns, ch):
    print(columns * ch)
    for i in range(1, rows - 1):
        print(ch, (columns - 2) * ' ', ch)
    print(columns * ch)


while True:
    try:
        height_of_the_rectangle = int(input("Введите высоту прямоугольника: "))
        width_of_the_rectangle = int(input("Введите ширину прямоугольника: "))
        char_for_rectangle = input("Введите символ для заливки прямоугольника: ")
        break
    except ValueError:
        print("Ширина и высота - целые числа!")

draw_rectangle(height_of_the_rectangle, width_of_the_rectangle, char_for_rectangle)

while True:
    try:
        height_of_the_triangle = int(input("Введите высоту треуголника: "))
        char_for_triangle = input("Введите символ для заливки треугольника: ")
        break
    except ValueError:
        print("Высота - целое число!")

draw_triangle(height_of_the_triangle, char_for_triangle)

while True:
    try:
        height_of_the_frame = int(input("Введите высоту рамки: "))
        width_of_the_frame = int(input("Введите ширину рамки: "))
        char_for_frame = input("Введите символ для заливки рамки: ")
        break
    except ValueError:
        print("Высота и ширина - целые числа!")

draw_frame(height_of_the_frame, width_of_the_frame, char_for_frame)
