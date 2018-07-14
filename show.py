import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import NullFormatter  # useful for `logit` scale


with open('0.log', 'r') as f:
    reader = csv.reader(f)
    dic = {}
    for i, row in enumerate(reader):
        if i == 0:
            for val in row:
                dic[val] = []
        else:
            dic['Mtr_Version'].append(row[0])
            dic['Start_Time'].append(row[1])
            dic['Status'].append(row[2])
            dic['Host'].append(row[3])
            dic['Hop'].append(int(row[4]))
            dic['Ip'].append(row[5])
            dic['Asn'].append(row[6])
            dic['Loss%'].append(float(row[7]))
            dic['Snt'].append(float(row[8]))
            dic[' '].append(row[9])
            dic['Last'].append(float(row[10]))
            dic['Avg'].append(float(row[11]))
            dic['Best'].append(float(row[12]))
            dic['Wrst'].append(float(row[13]))
            dic['StDev'].append(float(row[14]))

print(len(dic['Avg']))

# x = range(len(dic['Avg']))
x = dic['Start_Time']
x = [int(z[-4:]) for z in x]
print(x)
x = np.array(x)
y = np.array(dic['StDev'])

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y, 'r')
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y, 'y')
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean(), 'g')
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y, 'c')
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)


plt.show()