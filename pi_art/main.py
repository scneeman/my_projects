# get digits of pi
# convert to ascii / decimal
# arrange into tuples of 3
# create 2d list of colors

# define any functions
def get_pi():
    f = open("pi_art/pi_million_digits.txt", "r")  # open the file for reading
    pi = f.read() # read the data into one long string
    f.close() # close the file to release memory
    # TODOclean up
    pi = pi.replace(".", "")
    pi = pi.replace("\n", "")
    pi = pi.replace(" ", "")
    return pi

pi = "314159"
cols = []
for digit in pi:


# call the get_pi function
# pi = get_pi()
# print(len(pi))
