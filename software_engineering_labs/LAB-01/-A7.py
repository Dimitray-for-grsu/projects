first_position1 = int(input())
second_position1 = int(input())
summ_of_positions1 = first_position1 + second_position1

first_position2 = int(input())
second_position2 = int(input())
summ_of_positions2 = first_position2 + second_position2

if (summ_of_positions1 % 2) == 0:
    color1 = "White"
else:
    color1 = "Black"

if (summ_of_positions2 % 2) == 0:
    color2 = "White"
else:
    color2 = "Black"

if color1 == color2:
    if color1 == "White":
        print("YES")
        print("White")
    else:
        print("YES")
        print("Black")
else:
    print("NO")
