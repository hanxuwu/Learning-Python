#%%
# Tips: 
# 1.collections.deque 可以用来保存有限的历史记录 from collections import deque 
# 2.deque(maxlen=N)可以创建一个固定长度的队列，当有新纪录加入而队列已满时会自动移除最老的那条记录
# In [13]:


from collections import deque
q=deque(maxlen=3)
q.append(1)
print(q)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

#%%
#Tips: appendleft 可以从左边添加
from collections import deque
w= deque(maxlen = 3)  
w.append(11)
w.append(12)
w.append(13)
print(w)
w.appendleft(10) #在左边添加
print(w)
w.pop() #默认弹出最右  
print(w)
w.append(12) # 在右边添加
print(w)