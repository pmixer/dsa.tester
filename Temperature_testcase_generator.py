# for https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1149

import random

pos_min, pos_max = -2**31, 2**31-1

temp_min, temp_max = -10000, 10000

station_num, query_num = 50000, 50000

stations = set()

while len(stations) < station_num:
    stations.add((random.randint(pos_min, pos_max), random.randint(pos_min, pos_max)))

with open("Temperature.in", "w") as f:
    f.write(str(station_num) + " " + str(query_num) + "\n")
    for x, y in stations:
        f.write("{} {} {}\n".format(x, y, random.randint(temp_min, temp_max)))

    for _ in range(query_num):
        x_min = random.randint(pos_min, pos_max)
        x_max = random.randint(x_min, pos_max)
        y_min = random.randint(pos_min, pos_max)
        y_max = random.randint(y_min, pos_max)
        f.write("{} {} {} {}\n".format(x_min, y_min, x_max, y_max))

