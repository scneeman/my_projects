# get digits of pi
# convert to ascii / decimal
# arrange into tuples of 3
# create 2d list of colors

import functions as f

# --- testing ---
# cols = []
# for i in range(0, len(pi), 3):
#     col = (ord(pi[i]), ord(pi[i+1]), ord(pi[i+2]))
#     cols.append(col)
# print(cols)


pi = f.get_pi()

# 577x577
# f.single_digit_to_ord(pi, 577, 577, "pi_art/out.jpg")

# 1000x1000
# f.single_digit_to_scaled_greyscale(pi, 1000, 1000, "pi_art/outgrey.png")

# 1000x1000
f.diff_in_digits_to_scaled_greyscale(pi, 1000, 1000, "pi_art/outgrey2.png")

