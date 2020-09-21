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
    cmd = 'g++ -o ' + problem + ext[os_id] + ' ' + problem + '.cpp'
    if problem == 'Temperature':
        cmd += ' temperature_lib.c'
    print(cmd)
    os.system(cmd)
