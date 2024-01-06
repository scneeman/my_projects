from PIL import Image 
import numpy as np
import random


def get_pi():
    f = open("pi_art/pi_million_digits.txt", "r")  # open the file for reading
    pi = f.read() # read the data into one long string
    f.close() # close the file to release memory
    # clean up
    pi = pi.replace(".", "")
    pi = pi.replace("\n", "")
    pi = pi.replace(" ", "")
    return pi


def single_digit_to_ord(pi, width, height, newname):
    pic = [[0]*width for _ in range(height)]
    count = 0
    for r in range(height):
        for c in range(width):
            # col = (ord(pi[i]), ord(pi[i+1]), ord(pi[i+2]))
            temp1 = int(pi[count])*28
            temp2 = int(pi[count + 1])*28
            temp3 = int(pi[count + 2])*28
            pic[r][c] = (temp1, temp2, temp3)
            count += 3

    save_file(pic, newname)


def single_digit_to_scaled_greyscale(pi, width, height, newname):
    pic = [[0]*width for _ in range(height)]
    count = 0
    for r in range(height):
        for c in range(width):
            temp = int(pi[count])*28 # scale digits 0-9 up to 0-252
            pic[r][c] = (temp, temp, temp)
            count += 1
    save_file(pic, newname)



def diff_in_digits_to_scaled_greyscale(pi, width, height, newname):
    pic = [[0]*width for _ in range(height)]
    count = 0
    for r in range(height):
        for c in range(width):
            prev_spot = int(pi[count-1])
            this_spot = int(pi[count])
            diff = this_spot - prev_spot
            val = 128 + diff*14
            pic[r][c] = (val, val, val)
            count += 1
    save_file(pic, newname)


# must be square
def spiral(pi, n, newname):
    start_row = n//2
    start_col = n//2
    row = start_row
    col = start_col
    num_times = 1
    row_v = -1
    col_v = 1
    pic = [[0]*n for _ in range(n)]
    current_value = 1

    # starting pixel
    temp = int(pi[current_value-1])*28 # scale digits 0-9 up to 0-252
    pic[start_row][start_col] = (temp, temp, temp)

    while num_times < n:
        for r in range(num_times):
            current_value += 1
            row += row_v
            temp = int(pi[current_value-1])*28 # scale digits 0-9 up to 0-252
            pic[row][col] = (temp, temp, temp)
        row_v *= -1
        for c in range(num_times):
            current_value += 1
            col += col_v
            temp = int(pi[current_value-1])*28 # scale digits 0-9 up to 0-252
            pic[row][col] = (temp, temp, temp)
        col_v *= -1
        num_times += 1

    # last time, only 'up' 
    for i in range(n-1):
        current_value += 1
        row += row_v
        temp = int(pi[current_value-1])*28 # scale digits 0-9 up to 0-252
        pic[row][col] = (temp, temp, temp)

    save_file(pic, newname)




def load_file(orig):
    im = Image.open(orig)
    #im.show() # does not work in replit?
    mat = np.array(im)
    return mat


def save_file(mat, filename):
    # print(mat)
    result = Image.fromarray(np.uint8(mat))
    result.save(filename)