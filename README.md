Thanks to [Prof. Deng](https://dsa.cs.tsinghua.edu.cn/~deng/) and TAs' great work, we have got access to THU's Data Structure and Algorithms+Computational Geometry courses hosted on [XuetangX](https://next.xuetangx.com/course/THU08091000384/), [Coursera](https://www.coursera.org/specializations/data-structures-algorithms-tsinghua) and [Edx](https://www.edx.org/course/computational-geometry). corresponding problem sets are freely accessible on [THUOJ](https://dsa.cs.tsinghua.edu.cn/oj/).

The problems are of high quality(and with Bilingual:English+Chinese problem statements) but hard to slove sometimes due to unavailibilty of STL and deliberately designed testcases. Although millions of students registered in these courses, few of us completed the coursework so far.

This repo is designed to help peers working on these problems, instead of providing source code, I choose to compile my submissions(after AC on THUOJ) for MacOS/Linux/Windows separately, and write testcase generators in python, providing these files online to make your life easier.

Pls use the repo in the following way:

```
0. Clone the repo(or just download the zip file).

1. Create your submission file (i.e. `Range.cpp`) and implement your algorithm.

2. Compile it by your local compiler(i.e. `g++ Range.cpp -o myRange`).

3. Test with sample input, compare your output with sample output. (i.e. `myRange < Range.in > myRange.out`, `vimdiff myRange.out Range.out`).

4. If you passed the default testcase, but failed on THUOJ, pls use `python Range_testcase_generator.py` and corresponding executable file to generate new testcases(will overwrite `Range.in`) and corresponding output(`Range.app/bin/exe < Range.in > Range.out`) to help you debugging.
```

Depending on your specific programming environment setting, pls feel free to use the testcase generators and executables in your own way(i.e. edit parameters in testcase_generators for customizing your testcase and use `FC` rather than `vimdiff` on windows as long as you could efficiently identify the detail for which your implementation behaves weirdly comparing to expected output) to AC problems :)

I have uploaded sample executables and testcase generators for MOOC DSA course and will make it complete sooner, THU/CST/Camp version of DSA related files and CG related files would be uploaded later. Pls join in to enjoy the GREAT COURSES :)