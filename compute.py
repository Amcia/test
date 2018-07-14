import csv
import matplotlib.pyplot as plt

def remove_reapeted(file):
    with open(file, 'r') as f:
        content = f.readlines()
        header = content[0]
        content = [x for x in content if x != header]
        content.insert(0, header)
        with open('mtr_computed.log', 'w') as fil:
            for line in content:
                fil.write(line)


def check_how_many_hops(file):
    tmp = 0
    with open(file, 'r') as f:
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            print(row)
            if rownum == 0:
                rownum = 1
                continue
            if int(row[4]) > tmp:
                tmp = int(row[4])
            else:
                break
    return tmp


def split_per_hop(file, hop_num):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        handler = {}
        rownum = 0
        for i in range(hop_num):
            handler[i+1] = open('{}.log'.format(i), 'a')
        print(handler)
        for row in reader:
            if rownum == 0:
                for hand in handler.values():
                    hand.write(','.join(row)[:-1]+'\n')
                rownum = 1
                continue
            else:
                handler[int(row[4])].write(','.join(row)+'\n')
        for i in handler.values():
            i.close()


remove_reapeted('mtr.log')
split_per_hop('mtr_computed.log', check_how_many_hops('mtr_computed.log'))


