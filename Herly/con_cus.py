from threading import Thread, current_thread #可以实现多个生产者和消费者同时
import time
import random #随机
from queue import Queue  #队列
# 使用消息服务器上常见
queue = Queue(5) #定义队列的长度


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)  #往指定的队列里面加数字
            print('生产者 %s 生产了数据 %s'%(name, num))
            t = random.randint(1, 3) #获取随机的时间
            time.sleep(t)
            print('生产者 %s 睡眠了 %s 秒'%(name, t))


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName() #提取消费者的线程名称
        global queue
        while True:
            num = queue.get() #读取队列，封装好了线程等待和同步的代码
            queue.task_done()
            print('消费者 %s 消耗了数据 %s' %(name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者 %s 睡眠了 %s 秒' %(name, t))


p1 = ProducerThread(name='p1')
p1.start()
p2 = ProducerThread(name='p2')
p2.start()
p3 = ProducerThread(name='p3')
p3.start()
c1 = ConsumerThread(name='c1')
c1.start()
c2 = ConsumerThread(name='c2')
c2.start()

