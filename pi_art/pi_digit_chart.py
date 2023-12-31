import functions as f

pi = f.get_pi()


# create a dictionary of {num:length}
ans = {}

for i in range(10):
    ans[i] = pi.count(str(i))


print(ans)


import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(list(ans.keys()))
# y = np.array(list(ans.values()))
x = list(ans.keys())
y = list(ans.values())
plt.bar(x,y)
plt.show()