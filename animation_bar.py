import math

import time
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "@" * int(percent) + "-" * (100 - int(percent))
    print(f"]r|{bar}| {percent:.2f}%", end="\r")

"""numbers = [x * 5 for x in range(2000,3000)]
result = []

progress_bar(0, len(numbers))
for i, x in enumerate(numbers):
    result.append(math.factorial(x))
    progress_bar(i+1, len(numbers))
"""
seconds = 60
x= 0
progress_bar(0, seconds)
while x<seconds:
    x+=1
    progress_bar(x,seconds)
    time.sleep(1)
