import math

# Parameters
num_points = 100  # Number of points in the spiral
diameter = 0.8  # Diameter of the spiral
length = 2
num_loops = 5  # Number of loops in the spiral
elevation = 1.5  # Elevation from the x-axis
number_of_drones = 2

point_spacing = length/num_points

radius = diameter / 2.0

# Generate spiral waypoints along the x-axis
for num_drones in range(number_of_drones):
    file_name = f"waypoints_cf0{num_drones + 1}.csv"
    with open(file_name, 'w') as file:
        for i in range(num_points):
            delta_angle = (2 * math.pi) * (num_drones / number_of_drones)
            angle = ((num_loops * 2 * math.pi * i) / num_points) + delta_angle
            x = i * point_spacing
            y = radius * math.cos(angle)
            z = radius * math.sin(angle) + elevation
            file.write(f"{x},{y},{z}\n")

print("waypoints csv generated")