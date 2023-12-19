def is_consecutive(a_list):
    for i in range(len(a_list)):
        if not isinstance(a_list[i], int):
            return 'Not a valid input.  Please submit a list of integers'
        if i == 0:
            continue
        elif a_list[i] != a_list[i-1] + 1:
            return False
    return True

def is_consecutive(a_list):

    """ is_consecutive(a_list) Takes a list of integers as its argument and returns True if
     all numbers are in consecutive order, otherwise returns False """
    #a_list = int(a_list)
    for i in range(1,len(a_list)):
        if int(a_list[i]) - int(a_list[i-1]) == 1:
            continue
        else:
            return False
    return True
    

num_list_src = input("Input a set of numbers, consecutive or non-consecutive with no spaces\
example:123456")
num_list_src1 = list(num_list_src)
print(num_list_src1)
if consecutive := is_consecutive(num_list_src1):
    print("consecutive set of numbers")
else:
    print("not a consecutive set")


    # Note: I wanted the list to take input from a user instead of putting in a default list.

def is_consecutive(a_list):
    """Sort the list of numbers from the min range given to the max range given"""
    for numbers in range (0, input_numbers):
        user_input = int(input())
        numbers_list.append(user_input)
    return sorted(a_list)  == list(range(min(a_list), max(a_list) + 1))

# Empty list to store numbers
numbers_list = []

# Input numbers
input_numbers = int(input("How many numbers do you want to check to see if they are consecutive? "))


# Call function
print("Please input " + str(input_numbers) + " numbers.\nPress 'Enter' after each number entry." )
print("Is this list consecutive?" , is_consecutive(numbers_list))
def is_leap_year(year):

    """ def is_leap_year(year) Takes int <year> as argument 
    and returns True if the year is a leap year """
    
    year = int(year)

    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False
    
year = input("Enter a year and I will tell you if it is\
a leap year: ")


if leap_year := is_leap_year(year):
    print(f"{str(year)} is a leap year")
else:
    print(f"{str(year)} is not a leap year")
