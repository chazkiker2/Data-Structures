from time import sleep

# floodfill
image_str = [
    "#########################"
    "#    ###                #"
    "#   #   #               #"
    "#  #   ####             #"
    "# #        #            #"
    "# #       #             #"
    "# ########   ####       #"
    "#           #  #       #"
    "#          #  #         #"
    "#########################"
]

image = []

for i in image_str:
    image.append(list(i))


def print_image():
    for i in image:
        print("".join(i))


# print_image()


# floodfill(4, 6, "*")  # should fill surrounding shape with astricts

# mark charc at row_i, col_i
# flood_fill(up)
# flood_fill(right)
# flood_fill(down)
# flood_fill(left)
#
# traverse until we find character that is not a space
def floodfill(matrix, row_i, col_i, charc):
    if matrix[row_i][col_i] != ' ':
        return  # return out

    matrix[row_i][col_i] = charc
    print_image()

    sleep(0.5)

    floodfill(matrix, row_i - 1, col_i, charc)  # up
    floodfill(matrix, row_i + 1, col_i, charc)  # down
    floodfill(matrix, row_i, col_i - 1, charc)  # right
    floodfill(matrix, row_i, col_i + 1, charc)  # right


floodfill(image, 4, 6, "*")
