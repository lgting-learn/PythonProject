import threading
import time
import queue

'''
queue是python的标准库，俗称队列
queue 实现线程安全，和多线程配合使用，先进先出的数据结构
列表和字典都属于线程不安全的容器

'''
'''
队列的创建：
1.可以指明队列中能存放的数据个数的上限：maxsize = 20
一旦达到上限，插入会导致阻塞，直到队列中的数据被消费掉。
就像排队，只有20个位置,如果有人加入，除非空位。
2.如果maxsize小于或者等于0，队列大小没有限制。放置多少数据都是可以的。

'''

q = queue.Queue(maxsize = 20)

for i in range(1,21):
    #将数据放入队列中
    q.put(i)
    q.put(i+20)
    
    
#遍历队列
while not q.empty():
    print(q.get())

 
