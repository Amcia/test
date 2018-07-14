from subprocess import call
import time


print(time.asctime(time.localtime(time.time())))
for i in range (2):
    call(["mtr", "-n", "-r", "-c10", "--csv", "-z", "8.8.8.8", ">>", "mtr.log"])
    print("completed")
    print(time.asctime(time.localtime(time.time())))

# | awk '{ print $2 $4 }'