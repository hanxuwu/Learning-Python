
#1.1 Unpacking a Sequence into Separate Variables
#%%
p=(4,5)
x,y = p
p

#%%
data = ['ACME',50,91.1,(2017,7,30)]
name,share,price,data = data
print(name)
print(data)

#%%
data = ['ACME',50,91.1,(2017,7,30)]
name,share,price,(year,month,day) = data
print(year)
print(year,day)

#%%
#Tips：只要对象可迭代，就可以执行分解操作
s ='Hello'
a,b,c,d,e=s
print(a)
print(e)

#%%
#Tips:可以用一个用不到的值来丢弃不用的变量
data = ['ACME',50,91.1,(2017,7,30)]
name,_,_,date=data
print(name)
print(_)
print(date)