import numpy as np
import matplotlib.pyplot as plt
import csv
from os import listdir
from os.path import isfile, join

path_dir = "data/14data/"

sizes = []
time = []
onlyfiles = [f for f in listdir(path_dir) if isfile(join(path_dir, f))]
index = 0
for file_name in onlyfiles:
        with open(path_dir + file_name, 'r', encoding="utf16") as csvin:
                csvin = csv.reader(csvin, delimiter=',')
                itercsvin = iter(csvin)
                next(csvin)
                time.append([])
                for row in itercsvin:
                        if (index == 0):
                                sizes.append(int(row[0]))
                        time[index].append(float(row[1]))
                index += 1
avarge_time = np.array(time)
avarge_time = avarge_time.mean(axis=0)
plt.figure()
plt.plot(sizes, avarge_time)
plt.xscale('log', basex=2)
plt.xlabel("size in byte")
plt.ylabel("pinned vs non-pinned ratio")
plt.title("Commute Time to and from the device")
plt.savefig(
        path_dir + ".pdf")
