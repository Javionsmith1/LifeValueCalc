# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 14:55:02 2025

@author: smithjl3
"""

### This code is meant to compare and contrast 2 area choices
###
from locationClass import Location
from morgageCalculator import morgageAmatorizationSchedule
# This portion compares home price
# Tax rate gotten from here: https://taxfoundation.org/data/all/state/tax-burden-by-state-2022/

Mississippi = Location('Mississippi', 225000, 2.5, 15, 101000, 9.8)
Maryland = Location('Maryland', 550000, 3.5, 8, 117000, 11.3)

APR = 6.5
yearsLeft = 30
locationList = [Mississippi, Maryland]



for i in range(len(locationList)):
    HousingCost = morgageAmatorizationSchedule(APR, locationList[i]averageHomePrice, yearsLeft)

