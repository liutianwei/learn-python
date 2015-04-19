#-*- coding:utf-8 -*-
#姓名： 刘天威
#学号： 1403050108
#班级： 通风一班
#第三次作业修改有关线性代数问题
import numpy as np
x=np.array([1,3,2])
y=np.array([-2,1,-1])
lx=np.sqrt(x.dot(x)) 
ly=np.sqrt(y.dot(y))
print lx,ly
cos_angle=x.dot(y)/(lx*ly) 
print cos_angle