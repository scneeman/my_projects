# 'spirals' up, right, down, left, repeat

n = 7
start_row = n//2
start_col = n//2
row = start_row
col = start_col
num_times = 1
row_v = -1
col_v = 1
pic = [[0]*n for _ in range(n)]
current_value = 1
pic[start_row][start_col] = current_value


while num_times < n:
    for r in range(num_times):
        current_value += 1
        row += row_v
        pic[row][col] = current_value
        print(row, col, current_value)
    row_v *= -1
    for c in range(num_times):
        current_value += 1
        col += col_v
        pic[row][col] = current_value
        print(row, col, current_value)
    col_v *= -1
    num_times += 1

# last time, only 'up' 
for i in range(n-1):
    current_value += 1
    row += row_v
    pic[row][col] = current_value
    print(row, col, current_value)

