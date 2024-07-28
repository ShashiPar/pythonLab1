def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year=None):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month == 2 and year is not None and is_leap_year(year):
        return 29
    else:
        return month_days[month - 1]

if __name__ == "__main__":
    month_name = input("Enter the month name: ").capitalize()
    month_index = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"].index(month_name) + 1
    
    if month_index == 2:
        year = int(input("Enter the year: "))
        days_in_month = get_days_in_month(month_index, year)
    else:
        days_in_month = get_days_in_month(month_index)
    
    print(f"The number of days in {month_name} is: {days_in_month}")
