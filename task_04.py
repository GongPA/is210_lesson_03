#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 04: Ternary Expressions"""

DAY = raw_input("Please choose the day : \n"
                "[1] Monday \n"
                "[2] Tuesday \n"
                "[3] Wednesday \n"
                "[4] Thursday \n"
                "[5] Friday \n"
                "[6] Saturday \n"
                "[7] Sunday \n")

TIME = int(raw_input("And the time (ex: 0630): \n"))

if TIME < 600 or DAY == '6' or DAY == '7':
    SNOOZE = True
else:
    SNOOZE = False

print ("SNOOZE mode will be {0}").format(SNOOZE)
