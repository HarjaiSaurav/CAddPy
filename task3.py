a=[1,10.4,100+3j,6877989866,800+98j,"This is me",[1,2,3,4,5],(2,3,5,6,8),"Hey! just cheking",100056.9855]
for i in a:
 print(type(i))

a=[1,10.4,100+3j,"This is me",[1,2,3,4,5]]
print(a[0:5])

a=[1,4,8,10,67]
print("The List before addition is : ",a)
print("Addition")
for i in range(len(a)):
 a[i]+=5
print("The List After addition is : ",a) 
print("Multiplication")
for i in range(len(a)):
 a[i]*=5
print("The List After Multiplication is : ",a)

x=[45,65,30,360,75]
print("Just Sorting The List First:")
for i in range(len(x)):
 for a in range(i+1,len(x)):
   if(x[i]>x[a]):
     x[i],x[a]=x[a],x[i]
   print(i,a)
print("Sorted List is :",x)
print("Lowest number in the list is:",x[0])
print("Highest number in the list is:",x[-1])

x=[45,65,30,360,75]
m=[]
print("list after removing the even numbers are:")
for i in x:
 if i%2!=0:
   m.append(i)
print(m)

x=[]
for i in range(1,31):
 x.append(i*i)
print(x[:5])
print(x[-5:])

x= [[1,3,5,7,9,10],[2,4,6,8]]
y=x[0][:-1]+x[1]
print(y)

a={1:10,2:20}
b={3:30,4:40}
c={}
c.update(a)
c.update(b)
print(c)

n=int(input("Enter any numnber"))
x={}
for i in range(1,n+1):
 x[i]=i*i
print(x)

x=input("Enter values")
print(x)
y_list=x.split(",")
print(y_list)
print(type(y_list))
n_tuple=tuple(y_list)
print(n_tuple)
print(type(n_tuple))
