#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 05: Compound Examples"""

from decimal import Decimal

NAME = raw_input("What is your name? \n").title()
PRINCIPLE = int(raw_input(
    "What is the amount of your principle (amount being borrowed)? \n"))
YEARS = int(raw_input("For how many years is this loan being borrowed? \n"))
QUALIFIED = raw_input("Are you prequalified for this loan? \n"
                      "[1] for YES \n"
                      "[0] for NO \n").upper()[:1]
if PRINCIPLE > 0:

    if 0 < PRINCIPLE <= 199999:
        FINDINTREST =100
    elif 200000 <= PRINCIPLE <= 999999:
        FINDINTREST =200
    elif PRINCIPLE >= 1000000:
        FINDINTREST = 300
                
    if 1 <= YEARS <= 15:
        FINDINTREST += 10
    elif 15 < YEARS <= 20:
        FINDINTREST += 20
    elif 20 < YEARS <= 30:
        FINDINTREST += 30
    if QUALIFIED == "1":
        FINDINTREST += 1
        QUALIFIED = 'Yes'
    elif  QUALIFIED == "0":
        FINDINTREST += 0
        QUALIFIED = 'No'

    RATE = { 111:0.0363,
             110:0.0465,
             121:0.0404,
             120:0.0498,
             131:0.0577,
             130:0.0639,
             211:0.0302,
             210:0.0398,
             221:0.0327,
             220:0.0408,
             231:0.0466,
             311:0.0205,
             321:0.0262}[FINDINTREST]


    P = Decimal(PRINCIPLE)
    r = Decimal(RATE)
    t = YEARS
    n = 12

    TOTAL = Decimal(P * ((1+(r/n)) ** (n * t)))
    TOTAL = round(TOTAL)

    prTOTAL = str('{0}{1:,.0f}'.format('$', TOTAL))
    prPRINCIPLE = '{0}{1:,.0f}'.format('$', P)
    prYEARS = str(t) + "yrs"



    REPORT = (
        'Loan Report for: {0}'
        '\n{1}'
        '\n\tPrincipal:        {2:>10}'
        '\n\tDuration:         {3:>10}'
        '\n\tPre-Qualified?:   {4:>10}'
        '\n'
        '\n\tTotal:            {5:>10}'
        ).format(NAME, '-' * 68, prPRINCIPLE, prYEARS, QUALIFIED, prTOTAL)
else:
    REPORT = "NONE"

print REPORT
