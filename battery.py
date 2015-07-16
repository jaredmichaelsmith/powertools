#!/usr/bin/python

import atexit
import sys
import subprocess
import multiprocessing


def battery_notifier():
    power_info = subprocess.check_output(['pmset','-g', 'ps'])
    if 'AC Power' in power_info:

    else if 'Battery Power' in power_info:


def kill_processes(running_processes):
    for p in running_processes:
        p.terminate()


def main():
    running_processes = []
    atexit.register(kill_processes)

    # Replace with argv check
    if True:
        p = mulitprocessing.Process(target=battery_notifier)
        p.start()
        running_processes.append(p)


if __name__=='__main__':
    main()

