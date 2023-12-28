from PIL import Image 
import numpy as np
import random


def get_pi():
    f = open("pi_art/pi_million_digits.txt", "r")  # open the file for reading
    pi = f.read() # read the data into one long string
    f.close() # close the file to release memory
    # TODOclean up
    pi = pi.replace(".", "")
    pi = pi.replace("\n", "")
    pi = pi.replace(" ", "")
    return pi


def single_digit_to_ord(pi, outfilename):
    pic = []
    for r in range(577):
        row = []
        for i in range(0,1731,3):
            col = (ord(pi[i]), ord(pi[i+1]), ord(pi[i+2]))
            row.append(col)
        pic.append(row)

    # print(len(pic[0]))
    # print(len(pic))

    save_file(pic, outfilename)


def single_digit_to_scaled_greyscale(pi, outfilename):
    pic = []
    count = 0
    for r in range(10):
        row = []
        for c in range(10):
            col = int(pi[count])*28 # scale digits 0-9 up to 0-252
            col = (col, col, col)
            count += 1
            row.append(col)
        pic.append(row)
        print(row)
    save_file(pic, outfilename)

def save_file(mat, filename):
    mat = np.array(mat)
    result = Image.fromarray(mat, 'RGB')
    result.save(filename)