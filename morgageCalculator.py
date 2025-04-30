# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 12:45:51 2025

@author: smithjl3
"""
### This function calculates the morgage amatorization schedule for your home

###
import matplotlib.pyplot as plt

def morgageAmatorizationSchedule(APR, principal, yearsLeft, extraPayment = 1000):
    
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
        # Allows for early payoff
        if principalList[i] <= 0: 
            break
        
        # Calculate interest for this month
        interest = principal * monthlyInterest
        interestList.append(interest)

        # Payment applied to principal
        principalPayment = payment + extraPayment - interest
        principal -= principalPayment
        principal = max(principal, 0)
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
    
    # Plots interest paid over time
    plt.figure(figsize=(12,6))
    plt.plot(interestList, label='Monthly Interest Paid ($)', color='orange')
    plt.title('Monthly Interest Paid Over Time')
    plt.xlabel('Month')
    plt.ylabel('Interest Paid ($)')
    plt.grid(True)
    plt.legend()
    plt.show()

    totalInterestPaid = sum(interestList)
    totalPaid = totalInterestPaid + principalList[0]
    
    # Prints some messages to screen to show you how badly you are gettig fucked
    print(f"Total interest paid over the life of the loan: ${totalInterestPaid:.2f}")  
    print(f"Total Paid Over {yearsLeft} Years: ${totalPaid:.2f}")
    
    
    # Returns some values you might want if you are using this function somewhere else
    return principalList, interestList, yearlyAmountList
        


# This is to test my fucntion
if __name__ == "__main__":
    a = morgageAmatorizationSchedule(5, 200000, 15)    