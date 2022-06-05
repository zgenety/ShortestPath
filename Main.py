from color import Color
from Picture import Picture

input_image = Picture("46.png")
output_image = Picture("462.png")
color = Color

start = input_image.find_start()
finish = input_image.find_finish()
max_path_for_all_picture = input_image.width * input_image.height
temporary_array = [[max_path_for_all_picture for i in range(input_image.width)] for j in range(input_image.height)]
temporary_array[start[0]][start[1]] = 0
need_to_finish = False

for n in range(max_path_for_all_picture):
    if need_to_finish:
        break
    for i in range(input_image.height):
        for j in range(input_image.width):
            if input_image.img_ar[i][j] != color.black() and temporary_array[i][j] >= max_path_for_all_picture:
                space_array = []
                try:
                    space_array.append(temporary_array[i-1][j])
                except IndexError:
                    pass

                try:
                    space_array.append(temporary_array[i+1][j])
                except IndexError:
                    pass

                try:
                    space_array.append(temporary_array[i][j-1])
                except IndexError:
                    pass

                try:
                    space_array.append(temporary_array[i][j+1])
                except IndexError:
                    pass



                temporary_array[i][j] = min(space_array) + 1
                if input_image.img_ar[i][j] == color.red() and temporary_array[i][j] < max_path_for_all_picture:
                    need_to_finish = True

for i in range(input_image.height):
    for j in range(input_image.width):
        output_image.color_pixel(i, j, input_image.img_ar[i][j])

x, y = finish
while True:
    if temporary_array[x][y] == 0:
        break
    output_image.color_pixel(x, y, color.blue())
    space_array = []

    try:
        space_array.append([temporary_array[x-1][y], x-1, y])
    except IndexError:
        pass

    try:
        space_array.append([temporary_array[x+1][y], x+1, y])
    except IndexError:
        pass

    try:
        space_array.append([temporary_array[x][y-1], x, y-1])
    except IndexError:
        pass

    try:
        space_array.append([temporary_array[x][y+1], x, y+1])
    except IndexError:
        pass

    for i in range(4):
        if space_array[i][0] == min([j[0] for j in space_array]):
            print(x, y)
            x = space_array[i][1]
            y = space_array[i][2]
            break

output_image.show()
