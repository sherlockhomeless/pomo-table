#!/usr/bin/env python3

import sys
from datetime import timedelta, datetime
from colorama import Fore

LENGTH_SESH = timedelta(minutes=25)
LENGTH_PAUSE = timedelta(minutes=5)
NUM_SESSIONS = 4

def printeroo():
    """
    Function printing NUM_SESSIONS with LENGTH_SESH/PAUSE
    """
    try:
        h, m = int(sys.argv[1]), int(sys.argv[2])
    except IndexError:
        print(Fore.RED + "give hour/minute of start time as parameter $1 and $2", file = sys.stderr)
        sys.exit(1)

    t = datetime(2021, 5, 1, hour=h, minute=m)
    for i in range(NUM_SESSIONS):
        t = add_sesh(t, i)
        if i != NUM_SESSIONS -1:
            t = add_pause(t, i)


def add_pause(t: timedelta, i: int) -> timedelta:
    """
    : param t: starting time of pause
    : param i: index counting pomodoro iterations
    """
    print_str = f"Pause {i+1} => {t.strftime('%H:%M')}-"
    t = t + LENGTH_PAUSE
    print_str += f'{t.strftime("%H:%M")}'
    print(print_str)
    return t


def add_sesh(t: timedelta, i: int) -> timedelta:
    """
    : param t: starting time of pause
    : param i: index counting pomodoro iterations
    """
    print_str = f"Session {i+1} => {t.strftime('%H:%M')}-"
    t = t + LENGTH_SESH
    print_str += f'{t.strftime("%H:%M")}'
    print(print_str)
    return t


if __name__ == '__main__':
    printeroo()
