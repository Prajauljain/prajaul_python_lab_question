import numpy as np 
arr=np.array([20,30,50,70]) 
a=arr.view() 
arr[0]=100 
print(arr) 
print(a) 
