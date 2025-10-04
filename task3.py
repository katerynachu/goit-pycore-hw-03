import re 

def normalize_phone(phone_number:str) -> str| None:

    #delete all characters except digits
    number= re.sub(r"\D","",phone_number)

    #if number starts with 380 we add +
    if number.startswith("380"):
        number= "+" + number

    #if number starts with 0 we add +38
    elif number.startswith("0"):
        number = "+38" + number

    #for other formats add +380    
    else:
         number = "+380" + number

    #if lengh phone number less then 13 its not a good number for SMS
    if len(number) ==13 :
        return number #good number
    return None #not a number -> skip


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
     "+067\\t123 4567",  
     "mynymber777",
]

#generate list of normalized numbers and skip None ones
sanitized_numbers = [num for num in (normalize_phone(n) for n in raw_numbers) if num]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
