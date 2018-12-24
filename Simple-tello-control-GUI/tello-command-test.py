from tello import Tello
import sys
from datetime import datetime
import time

start_time = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())

f = open('command.txt', "r")
commands = f.readlines()

tello = Tello()
for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            print('delay %s'%(sec))
            time.sleep(sec)
            pass
        else:
            tello.send_command(command)

log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')

for stat in log:
    stat.print_stats()
    str1 = stat.return_stats()
    out.write(str1)
out.close()
