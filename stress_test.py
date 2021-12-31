import time
start_time = time.time()
times = []
index = 0
import os
while index != 100:
    import os
    os.system("python fox.py -i testfile.fox")
    with open('debug.log','r') as f:
        times.append(f.read().replace(" ","").replace("RunTime:","").replace("seconds","").replace("\n",""))
    f.close()
    index = index + 1
average = 0
for time in times:
    average = average+float(time)
average = "%.100f" % (average/index)
print(average)
import time
run_time = time.time() - start_time
print(run_time)
print("Program loss: "+str(float(run_time)-float(average)*100))