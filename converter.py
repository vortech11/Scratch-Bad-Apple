from os import path
from PIL import Image

image_name = 'output_'

scale = 2
printlist = []
filesize = (0, 0)

current_directory = path.dirname(path.abspath(__file__))


file_path = path.join(current_directory, "output.txt")
output = open(file_path, "w")
output.write("")
output.close()
output = open(file_path, "a")


for current_frame in range(6570):
    frame_output = ""
    file_path = path.join(current_directory, "frames/" + image_name + str(current_frame+1).zfill(4) + ".jpg")
    im = Image.open(file_path)
    im.thumbnail((im.size[0]/scale, im.size[1]/scale), Image.Resampling.LANCZOS)
    size = im.size
    pix = im.load()

    for y_index in range(size[1]-1, -1, -1):
        for x_index in range(size[0]):
            if pix[x_index, y_index][0] > (255/2):
                frame_output += str(1)
            else:
                frame_output += str(0)

    output.write("\n" + frame_output)
    filesize = size
    im.close()

print(filesize)
print("Done")