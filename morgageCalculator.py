# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 12:45:51 2025

@author: smithjl3
"""
### This function calculates the morgage amatorization schedule for your home

###
import matplotlib.pyplot as plt

def morgageAmatorizationSchedule(APR, principal, yearsLeft):
    
    APR = APR/100 # so you dont have to put gross decimals in
    monthsLeft = yearsLeft * 12 # calulcuates the amount in months
    monthlyInterest = APR/12
    
    # Calculates monthly payment based on what you provided
    payment = (principal* monthlyInterest*(1+monthlyInterest)**monthsLeft)/ ((1+monthlyInterest)**monthsLeft-1)
    print(f"Monthly payment: ${payment:.2f}")
    
    # initalize the lists needed for analysis
    yearlyAmountList = [] 
    interestList = []
    principalList = [principal]
    cumulativeInterest = 0
    cumulativeInterestList = [0]
    
    # Loops through all the months
    for i in range((monthsLeft)):
        
        # Calculate interest for this month
        interest = principal * monthlyInterest
        interestList.append(interest)

        # Payment applied to principal
        principalPayment = payment - interest
        principal -= principalPayment
        principalList.append(principal)
        cumulativeInterest += interest
        cumulativeInterestList.append(cumulativeInterest)
        
        if (i+1) % 12 == 0:
            yearlyAmountList.append(principal)
    
    
    
    # This does the plotting!
    # Plots the principle remaining on a yearly basis
    plt.figure(figsize=(12,8))
    plt.plot(principalList, label='Remaining Principal ($)')
    plt.plot(cumulativeInterestList, label='Cumulative Interest Paid ($)')
    plt.title('Mortgage Amortization Breakdown')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.grid(True)
    plt.legend()
    plt.show()
    
    plt.figure(figsize=(12,6))
    plt.plot(interestList, label='Monthly Interest Paid ($)', color='orange')
    plt.title('Monthly Interest Paid Over Time')
    plt.xlabel('Month')
    plt.ylabel('Interest Paid ($)')
    plt.grid(True)
    plt.legend()
    plt.show()

    totalInterestPaid = sum(interestList)
    totalPaid = totalInterestPaid + principal
    print(f"Total interest paid over the life of the loan: ${totalInterestPaid:.2f}")  
    print(f"Total Paid Over {yearsLeft} Years is {totalPaid}")
    
    
    # Returns some values you might want
    return principalList, interestList, yearlyAmountList
        


# This is to test my fucntion
if __name__ == "__main__":
    a = morgageAmatorizationSchedule(5, 100000, 30)    