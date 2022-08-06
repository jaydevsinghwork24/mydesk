import numpy as np
arr = np.array([9,2,7,4,6,8])
small = arr[0]
for i in range(len(arr)):
    if small > arr[i]:
        small=arr[i]
print('smallest is ', small)
