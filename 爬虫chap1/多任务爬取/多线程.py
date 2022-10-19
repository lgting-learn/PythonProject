import threading
import time

def listening():
    for i in range(5):
        print("我在听歌")
        # dd()
        time.sleep(1)

def reading():
    for i in range(5):
        print("我比较喜欢读书")
        time.sleep(1)
        


if __name__ == "__main__":
    
    t1 = threading.Thread(target = listening)
    t2 = threading.Thread(target = reading)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    #等待子线程执行结束之后再让主线程执行


    print("程序执行结束")
    
'''

#创建一个类，继承threading.Thread线程类
class MyThread(threading.Thread):

    #初始化父类的__init__方法
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name  #它是实例变量，存在对象t1,t2中
    def run(self):  #run就是父类的方法的重写
        print("正在执行—1\n")
        time.sleep(1)
        print("正在执行—2\n")
        time.sleep(1)
        print("正在执行—3\n")
        time.sleep(1)
        print("正在执行—4\n")
        time.sleep(1)
        print("正在执行—5\n")
        time.sleep(1)
        print("正在执行—6\n")
        time.sleep(1)
        print("正在执行—7\n")
        time.sleep(1)
        print("正在执行—8\n")
        time.sleep(1)
        print("正在执行—9\n")
        time.sleep(1)
        print("正在执行—10\n")
        time.sleep(1)
      

if __name__ == "__main__":
    
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t3 = MyThread("t3")
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("程序执行结束")
'''  


    
