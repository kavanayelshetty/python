import numpy as np

a=2
b=3
var=np.add(a,b)
print(np.subtract(a,b))
print(np.divide(a,b))
print(var)

arr_1=np.array([1,2,3,4])
print(arr_1)
print( )
print(np.array([[1,2,3,4],[1,2,3,4]]))
print( )
print(np.array([[[1,4,5,7],[5,6,74,8]]]))

arr_2=np.array([1,2,3,4])
print(np.cos(arr_2))
print(np.cumsum(arr_2))

import numpy as np
v1 = np.array([1,2,3,4])
v=np.insert(v1,(2,4),60)
print(var,v)

v2=np.array([[1,4,6],[2,5,7]])
v3=np.insert(v2,(2,4),19)
print(v3)
print(v2)

x=np.array([[1,2,5],[3,4,5]])
y=np.append(x,[[8],[9]],axis=1)
print(x)
print(y)

num = 18

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

