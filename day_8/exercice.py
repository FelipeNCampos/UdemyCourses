def years_to_weeks(years):
    return int((90 - int(years))*52)

    
def life_in_weeks(n):
    n = years_to_weeks(n)
    print(f"You have {n} weeks left.")
    
life_in_weeks(input())