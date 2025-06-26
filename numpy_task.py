import random
from tkinter import Y
import types
import numpy as np

#Q1
print(np.__version__)
#Q2
a=  [12.23, 13.32, 100, 36.32] 
b = np.array(a)
print(b.dtype)
#Q3
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c.shape)
#Q4
a = np.zeros(10)
a[5]=11
print(a)
#Q5
a = np.array(range(12,38))
print(a)
#q6
for i in range(int(len(a)/2)):
    temp = a[i]
    a[i]= a[len(a)-1-i]
    a[len(a)-1-i]=temp
print(a)
#q7
a = np.array(range(5))
print(a.dtype)
a = a.astype(np.float16)
print(a.dtype)
#q8
a = np.ones((5,5))
a[1:-1,1:-1]=0
print(a)
#q9
a= np.ones((3,3))
a = np.pad(a,pad_width=1,mode='constant',constant_values=0)
print(a)
#q10
a = np.zeros((8,8))
for i in range(8):
    for j in range(8):
        if j%2 !=0:
            a[i,j]=1
print(a)
#q11
a = list([1,2,3,4,5])
print(type(a))
a =np.asarray(a)
print(type(a))
a= ([1,2,3],[4,5,6])
print(type(a))
a = np.asarray(a)
print(type(a))
#q12
a = np.array([10,20,30])
a = np.append(a,[40,50,60])
print(a)
#q13
a = np.empty((3,2))
print(a)
b = np.full_like(a,6)
print(b)
#q14
a = np.array([0, 12, 45.21, 34, 99.91])
for i in range(len(a)):
    a[i] = (a[i]*9/5)+32
print(a)
print()
#q15
b = np.sqrt([0+1j])

print(b.real)
print(b.imag)

#q16
print("the size of the array",b.size)
print("length of one elemnt in the array is ",a.itemsize)
print("size of the total length ",a.nbytes)
#q17
a =np.array([0,10,20,30,40])
b=np.array([0,10])
print(np.isin(a,b))
#q18
print(np.intersect1d(a,b))
#q19
c =np.array([10,10,20,30,40,40,60])
print(np.unique(c))
#q20
print(np.setdiff1d(a,b))
#q21
print(np.setxor1d(a,b))
print()
#q23
a = np.array([10,20])
b=np.array([20,30,40,50])
print(np.union1d(a,b))
#q23
print(a.all())
#q24
print(a.any())
#q25
print(np.append(a,a))
#q26
print(np.repeat(a,2))
#q27
a=np.array([69,2000,10,1])
print(a.argmin())
print(a.argmax())
#q28
print()
print(a)
print(b)
print(a>b)
print(a<b)
#q29
a =np.array([[5,2],[3,1]])
print(np.sort(a,axis=1))#row sort
print(np.sort(a,axis=0))#column sort
#q30
a = np.array([[0,10,20],[20,30,40]])
print(a[a>10])
print(np.nonzero(a>10))
#sorting and searching
#started with question 2
#q31
dtypes= [('name','S4'),('class','i2'),('height','f2')]
a = np.array([('James', 5, 48.5 ) ,('Nail', 6, 52.5 ) ,('Paul', 5, 42.1 )
,('Pit', 5, 40.11)],dtype=dtypes)
a = np.sort(a,order='height')
print(a)
#q32
print()
a = np.sort(a,order=['class','height'])
print(a.dtype)
#q33
types = [('id','int16'),('height','float16')]
a = np.array([(1023,40.0),
(5241,40.0),
(1671,41.0),
(4532,42.0),
(5202,42.0),
(1682,38.0),
(6230,45.0)],dtype=types)
a = np.sort(a,order='height')
print(a)
#q34
print()
a = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
print(np.argsort(a))
#q35
a = np.array([(1+2j), (3-1j), (3-2j), (4-3j), (3+5j)])
a = np.sort_complex(a)
print(a)
#q36
b =np.array([ 70,50, 20, 30,-11, 60, 50, 40])
b =np.partition(b,5)
print(b)
#q37
a = np.random.rand(10)
print()
print(a)

print(np.partition(a,5))

#q38
a = np.array([[1,5,0],
[3,2,5],
[8,7,6]])
print(a[a[:,1].argsort()])
#q39
#from numpy random
a = np.random.normal(size=5)
print(a)

#40
a = np.random.randint(0,10,size=10)
print(a)
#41
a= np.random.random((3,3,3))
print(a)
#q42
print()
print()
a = np.random.random((5,5))
print(a.min())
print(a.max())
#q43
a = np.random.random((10,4))
print(a[:4,:])
#q44
a = np.arange(10)
a=np.random.shuffle(a)
print(a)
#q45
a = np.random.random(10)
min = a.min()
max = a.max()
print("Before normalization: ",a)
a = (a-min)/max-min
print("after: ",a)
#q46
a= a.sort(axis=0)
print("after sorting: ",a)
#47
a = np.array([1,0,1,0,1,1])
b= np.array([0,0,1,1,1,0])
print(np.allclose(a,b))
#48(11)
a = np.random.randint(0,100,size=10)
print(a)
maxindex = a.argmax()
a[maxindex]=-1
print(a)
#49(13)
a= np.random.randint(0,10,size=20)
print(a)
print()
modecount_index = np.unique(a,return_counts=True)[1].argmax()
mode = np.unique(a)[modecount_index]
print(mode)
#50
a = np.random.random((10,2))
col1,col2= a[:,0],a[:,1]
b = np.sqrt(col1**2+col2**2)
c = np.arctan2(col2,col1)
print(b)
print(c)


