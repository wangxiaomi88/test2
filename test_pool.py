import multiprocessing
import os
import time


def fun(msg):
    time.sleep(2)
    print(os.getpid(), ":", msg)
    return msg


pool = multiprocessing.Pool(4)

for i in range(10):
    msg = "haha{}".format(str(i))
    r = pool.apply_async(fun, args=(msg,))

pool.close()
pool.join()

print(r.get())

pool=multiprocessing.Pool()
r=pool.map(func=fun,iterable=[2,5,7])

print(r)