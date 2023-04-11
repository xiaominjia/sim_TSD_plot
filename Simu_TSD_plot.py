import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

now = datetime.now()
print(now)

date = datetime.today()
print(date)
Name = str(input('Please input the file name:(date is not needed)'))
# (Material/Voltage/Capacitor/Distance/Heat/R_measure/R_total)


# funciton1: set conditions
PreC = int(input('Please type "1" to set the condition'
                       ' or "0" to keep pre-set conditions'
               '(Interval = 5, Max-T= 300 C) or "2" for fast test:'))
if PreC == 1:
    Interval = int(input('please input Interval:'))
    MaxTemperature = int(input('please input Max temperature:'))
elif PreC == 0:
    Interval = 5
    MaxTemperature = 300
elif PreC == 2:
    Interval = 2
    MaxTemperature = 20.2
else:
    print ('Please input correct number')


N = int((MaxTemperature-20)*60/Interval)  # number of measurement

N = int(1.5 * N)

print(N)


#2:configuration for dev1&2


time.sleep(3)   # wait for reaction111

# 3:get data
start_time = time.time()


#plt.axis([0,N*Interval,0,1])
plt.ion()

for i in range(N):
    T = np.random.random()

    t = time.time() - start_time
    #plt.axis([0, t, 0, 1])
    plt.scatter(t,T)
    plt.autoscale()
    plt.pause(Interval-1)

plt.savefig(str(date.year)+str(date.month)+str(date.day)+str(Name)+'.pdf',format='pdf')
