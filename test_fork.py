import os
import time
a=1
pid = os.fork()

# time.sleep(0.1)

if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("新的进程")
    a+=20
    print("a=",a)
else:
    time.sleep(1)
    print("老的进程")
    print("a=",a)

print("结束")
