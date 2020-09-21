# for https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1151

import random

testcase_num = 1000

array = list(range(1, 9))

with open("Toy.in", "w") as f:
    f.write(str(testcase_num) + "\n")
    for i in range(testcase_num):
        f.write(" ".join([str(i) for i in array]) + '\n')
        random.shuffle(array)

