import numpy as np
arr = np.array([9,2,7,4,6,8])
small = arr[0]
# loop to find smallest number
for i in range(len(arr)):
    if small > arr[i]:
        small=arr[i]
print('smallest no is ', small)
