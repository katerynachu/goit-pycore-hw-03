from datetime import datetime,timedelta


def get_upcoming_birthdays(users:list) -> list :
    #today date
    today_date = datetime.today().date()

    #empty list for saving birthdays for this week
    upcoming_birthdays = []

    for user in users:
        #getting user birthday as date object
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=today_date.year)

        #if birthday already happened this year , we're looking for next year's date
        if birthday_this_year < today_date:
            birthday_this_year = user_birthday.replace(year = today_date.year + 1)

        #how many days left until birthday    
        delta_days = (birthday_this_year - today_date).days

        #checking if birthday is within next 7 days
        if 0 <= delta_days <=7:
            congrats_date = birthday_this_year

            #if birthday is on weekend,moving to Monday
            if congrats_date.weekday() >=5:
                days_to_monday = 7 - congrats_date.weekday()
                congrats_date+= timedelta(days = days_to_monday)

            # mapping birthday data into the result list
            upcoming_birthdays.append({
                "name" : user["name"],
                "congratulation_date" : congrats_date.strftime("%Y.%m.%d")
            }) 

    return upcoming_birthdays

#test 
users = [
    {"name": "John Doe", "birthday": "1985.10.5"},
    {"name": "Jane Smith", "birthday": "1990.10.17"}
]



upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
