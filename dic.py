import numpy as np
var=np.array([[[1,2,3],[0,9,6],[3,9,5],[7,6,1]]])
print(var)

var2 = np.array([1,2,3])
for i in np.nditer(var2,op_flags=['readwrite']):
    i[...]=i*2
print(var2)

arr = np.array([[1,2],[2,4]])
it=np.nditer(arr,flags=['multi_index'])
for x in it:
    print(it.multi_index,x)    