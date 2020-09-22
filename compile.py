import os
import sys
import platform

os_id = 'mac'
os_info = platform.platform().lower()
if 'linux' in os_info:
    os_id = 'linux'
elif 'windows' in os_info:
    os_id = 'windows'

ext = {'mac': '.app', 'linux': '.bin', 'windows': '.exe'}

mooc_problems = ['Range', 'Zuma', 'LightHouse',
                'Train', 'ProperRebuild', 'TSP',
                'Broadcast', 'Temperature', 'Deduplicate',
                'Toy', 'Schedule', 'Cycle']

for problem in mooc_problems:
    compiler = 'g++'
    if os_id == 'windows':
        compiler = "cl "
    compile_cmd = compiler + ' -o ' + problem + ext[os_id] + ' ' + problem + '.cpp'
    if problem == 'Temperature':
        compile_cmd += ' temperature_lib.c'
    print(compile_cmd)
    os.system(compile_cmd)

for problem in mooc_problems:
    exec_cmd = problem + ext[os_id]
    if problem != 'Temperature':
        exec_cmd += ' < ' + problem + '.in'
    print(exec_cmd)
    os.system(exec_cmd)