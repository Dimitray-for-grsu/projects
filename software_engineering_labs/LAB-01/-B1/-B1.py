import math

input_data = open("inmap0.dat", "r")

configuration_of_problem = input_data.readline().split()
number_of_locations = int(configuration_of_problem[0])
scale = float(configuration_of_problem[1])
list_of_distances_between_points = [line.strip() for line in input_data]
list_of_scaling_distances_between_points = []
summary_way = 0

for i in range(0, number_of_locations):
    list_of_scaling_distances_between_points.append(math.ceil((float(list_of_distances_between_points[i]) * scale) * 10) / 10)
for i in range(0, number_of_locations):
    summary_way = summary_way + list_of_scaling_distances_between_points[i]

input_data.close()

output_data = open("outmap0.dat", "x")
output_data.write("Gerasimchick Dmitrey. \n")
output_data.write("Simple Map Distance Computations. \n")
output_data.write("\n")
output_data.write(f"Map Scale Factor:     {scale} miles per inch \n")
output_data.write("\n")
output_data.write("     Map     Mileage \n")
output_data.write("     Measure  Distance\n")
output_data.write("====================================================\n")
for i in range(0, number_of_locations):
    output_data.write("#  {}    {:5}{:5}\n".format((i + 1), list_of_distances_between_points[i], list_of_scaling_distances_between_points[i]))
output_data.write("====================================================\n")
output_data.write(f"Total Distance:    {summary_way} miles")
output_data.close()