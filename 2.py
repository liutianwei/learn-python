import numpy as np
x=np.array([1,3,2])
y=np.array([-2,1,-1])
lx=np.sqrt(x.dot(x)) 
ly=np.sqrt(y.dot(y))
print lx,ly
cos_angle=x.dot(y)/(lx*ly) 
print cos_angle