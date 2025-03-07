## This script is the beginning of creating your financial outlook for your life
# God I'm drunk as shit! Let's GOOOOOOOOOOO

# Creates a class that holds bills
class Bills:
    def __init__(self, name, amount, occurrence, category, is_recurring):
        self.name = name  # Bill name
        self.amount = amount  # Amount due
        self.occurrence = occurrence  # How often it's due (e.g., "Monthly")
        self.category = category  # Type (e.g., "Rent", "Utilities")
        self.is_recurring = is_recurring  # Boolean: True/False

    def __int__(self):  # Allows sum() calculations
        return int(self.amount)

    def __str__(self):  # Prints a user-friendly summary
        return f"This bill is {self.name}, it is ${self.amount:,.2f}, and is due {self.occurrence}."


# This class holds your assets (stuff you own)
class Assets:
    def __init__(self, name, amount, rate_of_return, principal, time):
        self.name = name
        self.amount = amount
        self.rate_of_return = rate_of_return  # Expressed as a decimal (e.g., 0.05 for 5%)
        self.principal = principal  # Fixed initial investment
        self.time = time  # Investment duration (years)

    def __int__(self):
        return int(self.amount)  # Allows sum() calculations

    # Calculates compound interest
    def compound_interest(self):
        """
        Uses the formula: A = P(1 + r/n)^(nt)
        A = final amount, P = principal, r = annual rate, n = times compounded per year, t = years
        """
        n = 1  # Assuming annual compounding
        return self.principal * (1 + self.rate_of_return / n) ** (n * self.time)

    # Returns a clean string representation
    def __str__(self):
        return (f"Asset: {self.name}, Value: ${self.amount:,.2f}, "
                f"Projected Value (w/ interest): ${self.compound_interest():,.2f}")


# This class holds your liabilities (debts you owe)
class Liabilities:
    def __init__(self, name, amount, interest_rate, time):
        self.name = name
        self.amount = amount
        self.interest_rate = interest_rate
        self.time = int(time)

    def __int__(self):
        return int(self.amount)  # Allows sum() calculations

    # Calculates total interest paid over time (Simple Interest)
    def interest_calc(self):
        total_interest_paid = self.amount * self.interest_rate * self.time
        total_paid = total_interest_paid + self.amount
        return total_paid

    def __str__(self):
        return (f"Liability: {self.name}, Owed: ${self.amount:,.2f}, "
                f"Total Paid Over {self.time} Years: ${self.interest_calc():,.2f}")


# This class holds your income
class Income:
    def __init__(self, yearly_income, raise_rate, time, taxrate):
        self.yearly_income = yearly_income  # Starting salary
        self.raise_rate = raise_rate  # Annual salary increase (as decimal)
        self.time = time  # Number of years
        self.taxrate = taxrate # put your effective taxrate, TAXATION IS THEFT
        
    def create_income_list(self):
        """
        Creates a list of income for each year, adjusting for raises.
        """
        income_list = [self.yearly_income- self.yearly_income*self.taxrate]
        for _ in range(1, self.time):  # Start at 1, since year 0 is already set
            new_income = income_list[-1] * (1 + self.raise_rate)
            income_list.append(new_income)
        return income_list

    def total_income_earned(self):
        """
        Returns the total sum of all income earned over the given time period.
        """
        return sum(self.create_income_list())

    def __str__(self):
        return (f"Starting Salary: ${self.yearly_income:,.2f}, Raise Rate: {self.raise_rate * 100:.1f}%, "
                f"Total Income Earned Over {self.time} Years: ${self.total_income_earned():,.2f}")
    
    
   # Create instances
rent = Bills("Rent", 1850, "1st of the Month", "Housing", True)
car_loan = Liabilities("Car Loan", 12000, 0.05, 5)
savings = Assets("Savings", 10000, 0.04, 10000, 5)
income = Income(55000, 0.05, 5, 20/100)

# Print them
print(rent)
print(car_loan)
print(savings)
print(income)

# See Income List Over Time
print("Yearly Income Breakdown:", income.create_income_list()) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
