import time
def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "@" * int(percent) + "-" * (100 - int(percent))
    print(f"]r|{bar}| {percent:.2f}%", end="\r")


seconds = 60
x= 0

progress_bar(0, seconds)
while x<seconds:
    x+=1
    progress_bar(x,seconds)
    time.sleep(1)
