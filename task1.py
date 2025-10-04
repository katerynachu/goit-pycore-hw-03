from datetime import datetime

def get_days_from_today(date):
    try:
        #today's date
        today_day = datetime.today().date()

        #changing str to datetime object
        datetime_object = datetime.strptime(date, "%Y-%m-%d").date()

        #calculating difference between today and date from user
        delta = today_day - datetime_object

        #returning amount days
        return delta.days 
    
    except ValueError:
        #if format incorect - show message
        return "Please provide correct type of date in format YYYY-MM-DD ,for example 2025-02-02"  
    

#test
print(get_days_from_today("2026-10-09"))
print(get_days_from_today("2022-10-09"))
print(get_days_from_today("two three one"))