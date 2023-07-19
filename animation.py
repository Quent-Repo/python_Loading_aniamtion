import time
import sys

y = 20
x = 0
z = "/|-\\"
while (x != y):
    x+=1
    print(x)
    for i in range(0, 2):
        sys.stdout.write("\rLoading " + z[0])
        time.sleep(.2)
        sys.stdout.write("\rLoading " + z[1])
        time.sleep(.2)
        sys.stdout.write("\rLoading  " + z[2])
        time.sleep(.2)
        sys.stdout.write("\rLoading " + z[3])
        time.sleep(.2)
print("\n done")
