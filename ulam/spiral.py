from PIL import Image 
import numpy as np

def is_prime(n):
    stop = int(n**0.5)
    prime = True
    i = 2
    while i <= stop and prime:
        if n%i == 0:
            prime = False
        i += 1
    return prime

# 999*999 almost 1000000
n = 999
start_row = n//2
start_col = n//2
row = start_row
col = start_col
num_times = 1
row_v = -1
col_v = 1
pic = [[(255,255,255)]*n for _ in range(n)]
current_value = 1

# starting pixel
pic[start_row][start_col] = (0, 255, 0)


while num_times < n:
    for r in range(num_times):
        current_value += 1
        row += row_v
        if is_prime(current_value):
            pic[row][col] = (255, 0, 0)
    row_v *= -1
    for c in range(num_times):
        current_value += 1
        col += col_v
        if is_prime(current_value):
            pic[row][col] = (255, 0, 0)
    col_v *= -1
    num_times += 1

# last time, only 'up' 
for i in range(n-1):
    current_value += 1
    row += row_v
    if is_prime(current_value):
        pic[row][col] = (255, 0, 0)


# save
result = Image.fromarray(np.uint8(pic))
result.save("ulam/out.png")