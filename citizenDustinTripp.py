# NAME:     Dustin Tripp
# DATE:     11/24/2020
# FILE:     citizenDustinTripp.py
# PURPOSE:  A program that determines if you are eligable to be in the senate or
#           The house of reps



def main():

    print("This program will tell you if you are eligible to be a Senator,")
    print("Represenative, or neither based on your standings")
    print()
    
    #vars that will hold the age and citizenship lenth in years
    age = int(input("Please enter your age in years: "))
    print()
    usCitizen = int(input("Please enter the number of years you have been a US citizen: "))
    print()

    #These desision structires will determine if you are allowed to hold one position,
    #both positions, or neither of the positions in government
    if age >= 30 and usCitizen >=9:
        print("You are able to become a US Senator!")
        print()
    if age >= 25 and usCitizen >= 7:
        print("You are able to become a US Represenative!")

    if age < 25 or usCitizen < 7:
        print("You are unable to hold a position in the Senate or the House at this time")

main()


input("Press <Enter> to quit ")



