def collatz(num):
    count = 0
    while num > 1:
        if num%2 == 0:
            num /= 2
        else:
            num = num*3 + 1
        count += 1
    return count

# create a dictionary of {num:length}
ans = {}
for num in range(2, 100):
    ans[num] = collatz(num)

print(ans)


import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(list(ans.keys()))
# y = np.array(list(ans.values()))
x = list(ans.keys())
y = list(ans.values())
plt.bar(x,y)
plt.show()