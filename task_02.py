#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02: Simple Branching"""

BP_STATUS = int(raw_input("Please input a blood pressure : "))

if BP_STATUS <= 90:
    BP_STATUS = "Low"
elif 90 < BP_STATUS <= 119:
    BP_STATUS = "Ideal"
elif 119 < BP_STATUS <= 139:
    BP_STATUS = "Warning"
elif 139 < BP_STATUS <= 160:
    BP_STATUS = "High"
elif BP_STATUS > 160:
    BP_STATUS = "Emergency"
else:
    BP_STATUS = "Pleas input a number."

print "Your blood pressure status is {0}.".format(BP_STATUS)
