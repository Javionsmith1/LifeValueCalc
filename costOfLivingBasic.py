def areaCompare(locationName1, locationName2, annualSalary1, annualSalary2,
                homePrice1, homePrice2, annualMileage, gasCost1, gasCost2):
    """
    Compare and contrast the cost of living between two areas based on:
    - Annual salary
    - Average home price
    - Estimated annual commute cost (based on local gas prices)

    Parameters:
    locationName1 (str): Name of the first location.
    locationName2 (str): Name of the second location.
    annualSalary1 (float): Annual salary in the first location.
    annualSalary2 (float): Annual salary in the second location.
    homePrice1 (float): Average home price in the first location.
    homePrice2 (float): Average home price in the second location.
    annualMileage (float): Estimated yearly driving mileage.
    gasCost1 (float): Cost per gallon of gas in the first location.
    gasCost2 (float): Cost per gallon of gas in the second location.

    Returns:
    tuple: Adjusted cost of living for location 1 and location 2.
    Lower value indicates more affordable living.
    """

    print(f"Doing comparison between {locationName1} and {locationName2}\n")

    # Commute costs
    commuteCost1 = annualMileage * gasCost1
    commuteCost2 = annualMileage * gasCost2

    # Adjusted cost of living = Home price + commute cost - salary
    adjustedCost1 = homePrice1 + commuteCost1 - annualSalary1
    adjustedCost2 = homePrice2 + commuteCost2 - annualSalary2

    print(f"{locationName1}:")
    print(f"  Annual Salary: ${annualSalary1:,.2f}")
    print(f"  Average Home Price: ${homePrice1:,.2f}")
    print(f"  Gas Price: ${gasCost1:.2f}/gallon")
    print(f"  Estimated Annual Commute Cost: ${commuteCost1:,.2f}")
    print(f"  Adjusted Cost of Living: ${adjustedCost1:,.2f}")

    print(f"\n{locationName2}:")
    print(f"  Annual Salary: ${annualSalary2:,.2f}")
    print(f"  Average Home Price: ${homePrice2:,.2f}")
    print(f"  Gas Price: ${gasCost2:.2f}/gallon")
    print(f"  Estimated Annual Commute Cost: ${commuteCost2:,.2f}")
    print(f"  Adjusted Cost of Living: ${adjustedCost2:,.2f}")

    print("\n--- Conclusion ---")
    if adjustedCost1 < adjustedCost2:
        print(f"{locationName1} has a more affordable adjusted cost of living.")
    elif adjustedCost2 < adjustedCost1:
        print(f"{locationName2} has a more affordable adjusted cost of living.")
    else:
        print("Both locations have the same adjusted cost of living.")

    return adjustedCost1, adjustedCost2




    
    
    