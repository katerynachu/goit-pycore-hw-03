import random


def get_numbers_ticket(min_number:int, max_number:int, quantity:int) -> list[int]:

    #checking if numbers are right
    if min_number >=1 and max_number <=1000 and quantity > 0 and quantity <= (max_number - min_number + 1):

        #generate random numbers 
        numbers = random.sample(range(min_number, max_number + 1), quantity)

        #return sorted numbers list
        return sorted(numbers)
    else:
        # if numbers are too high or invalid, return empty list
        return []
    
#test    
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lucky numbers are ", lottery_numbers)


try:
    #asking user to input numbers and changing str to int
    min_number = int(input("Please Enter minimum number  "))
    max_number = int(input("Please Enter maximum number  "))
    quantity = int(input("Please Enter how many numbers do you want "))

    #calling function to create some lucky numbers using data provided by user
    lottery_numbers = get_numbers_ticket(min_number, max_number, quantity)

    #print numbers if they'are excist
    if lottery_numbers:
        print("Your lucky numbers are ", lottery_numbers)

#show error if user input something other than numbers
except ValueError :
    print("Please provide numbers!Only numbers accepted")

