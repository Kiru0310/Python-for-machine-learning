import numpy as np
a = np.array([[1,2,4],[5,8,7]])
print ("Array created using passed list:\n",a)




b = np.zeros((3,4))
print("nAn array initialized with all zeros:\n",b)


c = np.full((3,3),6)
print("\nAn array initialized with all 6s.\n",c)


d = np.random.random((2,2))
print("\nA random array:\n",d)


e = np.arange(0,30,5)
print("\n A sequential array with steps of 5:\n",e)


arr = np.array([[1,2,3,4],[5,2,4,2],[1,2,0,1]])
newarr = arr.reshape(4,3)
print("\nOriginal array:\n",arr)
print("Reshaped array[4,3]:\n",newarr)




flarr = arr.flatten()
print("\nOriginal array:\n",arr)
print("Fattened array:\n",flarr)



print("\nNo. of dimensions:",arr.ndim)

print("\nSize of array:",arr.shape)

print("\nArray stores elements of type:",arr.dtype)

newtype=arr.astype('f')
print("\nConverted array elements:\n",newtype)
print("Converted array type:",newtype.dtype)



import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[30:0:-1])



import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[2,0:2])



import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[2:,2:])


import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[3:,3:])

import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
print(p[:,1])

import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
c=p.astype('f')
print(c)

import numpy as np
p=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]])
c=p.astype('i')
print(c)



