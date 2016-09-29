# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import psutil
import time
import sys
from subprocess import check_output
import chardet


def multiplatform_vmstat(count):
    """Get data in a multiplatform way
    """
    cpu_percent, io_stat, io_stat_0 = 0, 0, 0
    print("cpu%", "iops(r+w)")
    for x in range(-count, 1):
        cpu_percent = psutil.cpu_percent()
        io_counters = psutil.disk_io_counters()
        read_io = io_counters.read_count
        write_io = io_counters.write_count
        io_stat = read_io + write_io
        print(cpu_percent, io_stat - io_stat_0)
        io_stat_0 = io_stat
        if x:
            time.sleep(10)


def grep(needle, fpath):
    """A simple grep implementation

       goal: open() is iterable and doesn't
             need splitlines()
       goal: comprehension can filter lists
    """
    return [x for x in open(fpath) if needle in x]


def igrep(expr, iterable):
    return [x for x in iterable if expr in x]


def sh(cmd, shell=False, timeout=0):
    """"Returns an iterable output of a command string
        checking...
    """
    from sys import version_info as python_version
    if python_version < (3, 3):  # ..before using..
        if timeout:
            raise ValueError("Timeout not supported until Python 3.3")
        output = check_output(cmd.split(), shell=shell)
    else:
        output = check_output(cmd.split(), shell=shell, timeout=timeout)

    # In mac os x we can have some accents in output (sáb)
    return [x.decode(chardet.detect(x).get('encoding')) for x in output.splitlines()]


def pgrep(program):
    # linux or mac
    if sys.platform.startswith('win'):
        return igrep(program, sh("tasklist"))
    else:
        return igrep(program, sh("ps -fe"))


diskstats_headers = ('major minor device'
                     ' reads reads_merged reads_sectors reads_ms'
                     ' writes writes_merged writes_sectors writes_ms'
                     ' io_in_progress io_ms_spent io_ms_weight').split()


def linux_diskstats(disk):
    """Get I/O information from /proc/diskstats
       @param disk def sda
       goal: usage of time.sleep
       goal: usage of dict.setdefault
       goal: use string concatenation to increase readability
       goal: use *magic with print+sep, splitting and slicing
    """
    from time import sleep
    info = ('reads reads_merged reads_sectors reads_ms'
            ' writes writes_merged writes_sectors writes_ms'
            ' io_in_progress io_ms_weight').split()
    print(*info, sep=",")
    old, cur = dict(), dict()
    while True:
        disk_l = grep(disk, "proc/diskstats")
        for x in disk_l:
            info = x.split()
            # the first 3 fields are disk informations
            part = info[2]
            old.setdefault(part, [0] * 11)
            cur[part] = map(int, info[3:])
            delta = [x - y for x, y in zip(cur[part], old[part])]
            print(*delta, sep=",")
            old[part] = cur[part]
        sleep(1)


def parse_line(line):
    import re
    _, _, hour, host, _, _, dest = line.split()[:7]
    try:
        dest = re.split(r'[<>]', dest)[1]
    except (IndexError, TypeError):
        dest = None
    return (hour, host, dest)

if __name__ == "__main__":
    print(pgrep("firefox"))
    linux_diskstats("vda1")
