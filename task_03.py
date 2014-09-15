#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task #03: Nested Statements"""

BASE = raw_input(
    "Please only input 1 or 2 for follwing questions! \n"
    "Please pick between 2 colors - \n"
    "[1] Seattle Gray or [2] Manatee? : ")

if BASE == "1":
    BASE = "Seattle Gray"
    ACCENT = raw_input("[1] Ceramic Glaze or [2] Cumulus Nimbus : ")
    if ACCENT == "1":
        ACCENT = "Ceramic Glaze"
        HIGHLIGHT = raw_input("[1] Basically White or [2] White : ")
        if HIGHLIGHT == "1":
            HIGHLIGHT = "Basically White"
        elif HIGHLIGHT == "2":
            HIGHLIGHT = "White"
    elif ACCENT == "2":
        ACCENT = "Cumulus Nimbus"
        HIGHLIGHT = raw_input("[1] Off-White or [2] Paper White : ")
        if HIGHLIGHT == "1":
            HIGHLIGHT = "Off White"
        elif HIGHLIGHT == "2":
            HIGHLIGHT = "Paper White"
elif BASE == "2":
    BASE == "Manatee"
    ACCENT = raw_input("[1] Platinum Mist of [2] Spartan Sage : ")
    if ACCENT == "1":
        ACCENT = "Platinum Mist"
        HIGHLIGHT = raw_input("[1] Bone White or [2] Just White : ")
        if HIGHLIGHT == "1":
            HIGHLIGHT = "Bone White"
        elif HIGHLIGHT == "2":
            HIGHLIGHT = "Just White"
    elif ACCENT == "2":
        ACCENT = "Spartan Sage"
        HIGHLIGHT = raw_input("[1] Fractal White or [2] Not White : ")
        if HIGHLIGHT == "1":
            HIGHLIGHT = "Fractal White"
        elif HIGHLIGHT == "2":
            HIGHLIGHT = "Not White"

print (
    '\n \nYour base color is {0}; \nYour accent is {1}; \n'
    'And your highlight is {2}.').format(BASE, ACCENT, HIGHLIGHT)
