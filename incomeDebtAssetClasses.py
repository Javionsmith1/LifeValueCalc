## This script is the beginning of creating your financial outlook for your life
# God I'm drunk as shit! Let's GOOOOOOOOOOO

# Creates a class that holds bills
class Bills:
    def __init__(self, name, amount, occurrence, category, is_recurring):
        self.name = name
        self.amount = amount
        self.occurrence = occurrence  # How often it's due (e.g., "Monthly")
        self.category = category  # Type (e.g., "Rent", "Utilities")
        self.is_recurring = is_recurring  # Boolean: True/False

    def __int__(self):
        return int(self.amount)  # Allows sum() calculations

    def __str__(self): # Prints you off a little sentence
        return f"This bill is {self.name}, it is ${self.amount:.2f}, and is due {self.occurrence}."


# This class holds your assets (stuff you own)
class Assets:
    def __init__(self, name, amount, rateOfReturn, principle, time):
            self.name = name
            self.amount = amount
            self.rateOfReturn = rateOfReturn
            self.principle = principle
            self.time = time

    def __int__(self):
        return int(self.amount)  # Allows sum() calculations
    
    # Calculates compound interest
    def compoundInterest(self):
        """
        Calculates compound interest using the formula:
        A = P(1 + r/n)^(nt)
        where:
        A = final amount
        P = principal (initial deposit)
        r = annual interest rate (decimal)
        n = number of times interest is compounded per year
        t = time in years
        """
        n = 1
        compoundInterest = self.principle*(1+self.rateOfReturn/n)**(n*self.time)
        return compoundInterest
    
    # Does the string return
    def __str__(self):
        return (f"Asset: {self.name}, Value: ${self.amount:.2f}, "
                f"Projected Value (w/ interest): ${self.compound_interest():.2f}")

# This class holds your liabilities (debts you owe)
class Liabilities:
    def __init__(self, name, amount, interestRate):
        self.name = name
        self.amount = amount
        self.interestRate = interestRate
        
    
    def __int__(self):
        return int(self.amount)  # Allows sum() calculations
    
    
    def 


# This class holds your income
class Income:
    def __init__(self, yearlyIncome):
        self.yearlyIncome = yearlyIncome




## We using this shit, I made everything objects, maybe this bitch coulda been a function, who knows


