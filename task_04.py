#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""redo task 4"""
DAY = raw_input("What day is it? : ").lower()[slice(0, 3)]
TIME = int(raw_input("What time is it? (ex: 0630): "))
if TIME < 600 or DAY == 'sat' or DAY == 'sun':
    SNOOZE = True
else:
    SNOOZE = False
print SNOOZE
