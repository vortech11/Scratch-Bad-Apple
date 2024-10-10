from os import path
from math import sqrt

aspect_ratio = 480/360 

current_directory = path.dirname(path.abspath(__file__))

file_path = path.join(current_directory, "output.txt")

output = open(file_path, "r")

file_path = path.join(current_directory, "compiled_output.txt")

compiled_output = open(file_path, "w")
compiled_output.write("")
compiled_output.close()
compiled_output = open(file_path, "a")

for line in output:
    output_frame = ""
    
    total_pixels = len(line)
    
    y_length = int(sqrt(total_pixels/aspect_ratio))
    x_length = int(y_length * aspect_ratio)

    for y_index in range(y_length):
        output_line = ""
        x_index = 0
        color = line[y_index * x_length]
        pixel_length = 0
        while x_index < x_length:
            if line[y_index * x_length + x_index] == color:
                pixel_length += 1
            else:
                output_line += str(pixel_length).zfill(3) + str(color)
                pixel_length = 0
                color = line[y_index * x_length + x_index]
            x_index += 1
        output_line += str(pixel_length).zfill(3) + str(color)
        output_frame += output_line
    
    compiled_output.write("\n" + output_frame)

print(x_length, y_length)
print("Done")