import  multiprocessing as mp
import time

def fun(sec):
    print("开始一个进程")
    time.sleep(sec)
    a=10000
    print("进程结束")


a=1
p=mp.Process(target=fun,args=(3,))
p.start()


time.sleep(1)
print("父进程执行")

p.join()
print("======================")
print(a)


