import time
import sys

def main():
    l = "\|/─"
    while 1:
        for i in range(0,len(l)):
            sys.stdout.write("\r " +l[i])
            time.sleep(.25)
main()
