
#1.2 Unpacking Elements from Iterables of Arbitrary Length
#%%
# Tips： 使用 *表达式
Marks=[1,2,3,4,5,6,7,8]
def drop_first_and_last(grade):
    first,*middle,last=grade
    return middle     # 写函数记得加返回值

drop_first_and_last(Marks)

#%%
#Tips:分解时不用考虑其不是列表的情况
record = ['Andrew','18','Andrew@gmail.com','0424554321','0434567897']
name,age,mail,*phone_number =record
phone_number

#%%
record=[('foo',1,2),('bar','hello'),('foo',4,5)]
def print_foo(x,y):   #记得加 冒号
    print(x,y)
def print_bar(s): # 未切换输入法  SyntaxError: invalid character in identifier
    print(s)
    
for (name,*args) in record:
    if name =='foo': # 记得加  冒号  否则  SyntaxError: invalid syntax
        print_foo(*args)   # 记得 缩进   否则  IndentationError: expected an indented block
    elif name =='bar':
        print_bar(*args)

#%%
#Tips:特定字符串的拆分操作
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
name,*fields,homedir,sh = line.split(':')
print(name)
print(homedir)
print(sh)

#%%
#Tips:丢弃多个变量
data = ['ACME',50,91.1,(2017,7,18)]
name,*_,(*_,split_day) = data
print(split_day)
