x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

if x_1 == 0 or x_2 == 0 or y_1 == 0 or y_2 == 0:
    print("Write correct data")

if x_1 < 0 and y_1 < 0: Label_1 = "III"
if x_1 > 0 and y_1 > 0: Label_1 = "I"
if x_1 > 0 and y_1 < 0: Label_1 = "IV"
if x_1 < 0 and y_1 > 0: Label_1 = "II"

if x_2 < 0 and y_2 < 0: Label_2 = "III"
if x_2 > 0 and y_2 > 0: Label_2 = "I"
if x_2 > 0 and y_2 < 0: Label_2 = "IV"
if x_2 < 0 and y_2 > 0: Label_2 = "II"

if Label_1 == Label_2:
    print("YES, ", Label_1)
