import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr)
print("dimensions=",arr.ndim)
print("shape=",arr.shape)

# now 3d dimensional
print("==============================")
print("======3d dimensional=======")
print("==============================")
import numpy as np
arr=np.array([
   [ [1,2,3],
    [4,5,6]],
    [[7,8,9],
     [1,5,8]]

])
print(arr)
print("dimensions=",arr.ndim)
print("shape=",arr.shape)

#vectorization
print("==============================")
print("======Vectorization======")
print("==============================")
import numpy as np
num=np.array([1,2,3,4,5])
result=num*2
print(result)

#broadcasting
print("==============================")
print("=========Broadcasting=========")
print("==============================")
import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
result=arr+5
print(result)

#Reshape
print("==============================")
print("=========Reshape=========")
print("==============================")
import numpy as np
num=np.array([1,2,3,4,5,6])
result=arr.reshape(2,3)
print(result)

#flatten
print("==============================")
print("=========flatten=========")
print("==============================")
import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
result=arr.flatten()
print(result)

#slicing
print("==============================")
print("=========slicing=========")
print("==============================")
import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr[1,1:3])

print("==============================")
print("=========Boolean masking=========")
print("==============================")
num=np.array([1,2,3,4,5,6])
result=arr>3
print("check if the num(1,2,3,4,5,6) is greater than 3 or not")
print(result)
even=num[num%2==0]
print("check if the num(1,2,3,4,5,6) is even or not")
print(even)

