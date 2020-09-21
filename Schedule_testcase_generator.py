# for https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1152
# in reference to https://pynative.com/python-generate-random-string/

import string
import random

MAX_STRING_LEN = 8
JOB_NUM = 10000 # n
OUTPUT_JOB_MAX = 10000000 # m

letters = string.ascii_lowercase + string.digits

job_names = set()

while len(job_names) < JOB_NUM:
    job_names.add("".join([random.choice(letters) for i in range(random.randint(1, MAX_STRING_LEN))]))

with open("Schedule.in", "w") as f:
    f.write("{} {}\n".format(JOB_NUM, OUTPUT_JOB_MAX))
    for job in job_names:
        f.write("{} {}\n".format(random.randint(1, 2**32-1), job))