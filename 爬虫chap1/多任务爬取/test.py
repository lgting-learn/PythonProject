# 单线程爬取时，获取一个url解析一个url，将信息写入文件。爬取数据较大时，应采用更高效的多线程爬取
# 多线程回顾
import threading
import time
from queue import Queue
#
#
# def listening():
#     for i in range(5):
#         print('listening')
#         time.sleep(1)
#
#
# def reading():
#     for i in range(5):
#         print('reading')
#         time.sleep(1)
#
#
# def main():
#     t1 = threading.Thread(target=listening)
#     t2 = threading.Thread(target=reading)
#     t1.start()
#     t2.start()
#     # 子线程与主线程随机执行，需要子线程执行结束再到主线程执行使用join()
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     main()
#     print('主线程结束')
q=Queue()

for i in range(5):
    q.put(i)

while not q.empty():
    print(q.get())
