import threading
import time
def thread_test1():
    print(f"T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print('T1 end')

def thread_test2():
    print("T2 start\n")
    print("T2 end\n")

if __name__ == '__main__':
    thread1 =threading.Thread(target=thread_test1,name='T1')
    thread2 = threading.Thread(target=thread_test2,name='T2')
    thread1.start()
    thread2.start()
    # join让后面的代码等待该线程结束才执行
    # thread1.join()
    thread2.join()
    thread1.join()
    print('all done')