from subprocess import call
import time


localtime = time.asctime(time.localtime(time.time()))
with open("mtr.log", 'w') as f:
    while '19:05:' not in localtime:
        call(["mtr", "-n", "-r", "-c10", "--csv", "-z", "8.8.8.8"], stdout=f)
        print("completed")
        localtime = time.asctime(time.localtime(time.time()))
