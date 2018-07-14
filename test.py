from subprocess import call
import time


print(time.asctime(time.localtime(time.time())))
with open("mtr.log", 'w') as f:
    for i in range (2):
        call(["mtr", "-n", "-r", "-c10", "--csv", "-z", "8.8.8.8"], stdout=f)
        print("completed")
        print(time.asctime(time.localtime(time.time())))
