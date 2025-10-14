Input_Value = int(input())
seconds = Input_Value % 3600 % 60
minutes = (Input_Value % 3600) // 60
hours = Input_Value // 3600
print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
