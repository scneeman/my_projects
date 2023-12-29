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


def single_digit_to_ord(pi, infilename, outfilename):
    pic = load_file(infilename)
    count = 0
    for r in range(577):
        for c in range(577):
            # col = (ord(pi[i]), ord(pi[i+1]), ord(pi[i+2]))
            temp1 = int(pi[count])*28
            temp2 = int(pi[count + 1])*28
            temp3 = int(pi[count + 2])*28
            pic[r][c] = (temp1, temp2, temp3)
            count += 3

    save_file(pic, outfilename)

# i had to load a 'dummy' image
# i don't know how to create an appropriate numpy array from a 2d list
def single_digit_to_scaled_greyscale(pi, infilename, outfilename):
    # pic = [[0]*1000 for _ in range(1000)]
    pic = load_file(infilename)
    count = 0
    for r in range(1000):
        for c in range(1000):
            temp = int(pi[count])*28 # scale digits 0-9 up to 0-252
            pic[r][c] = (temp, temp, temp)
            count += 1
    save_file(pic, outfilename)


def load_file(orig):
    im = Image.open(orig)
    #im.show() # does not work in replit?
    mat = np.array(im)
    return mat


def save_file(mat, filename):
    # print(mat)
    result = Image.fromarray(mat, 'RGB')
    result.save(filename)