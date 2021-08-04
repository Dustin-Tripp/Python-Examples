# NAME:     Dustin Tripp
# DATE:     11/24/2020
# FILE:     validDateDustinTripp.py
# PURPOSE:  A program that determines if s date is valid

#----------This function determines if a year is a leap year or not------#
def leapYear(year):

    if (year % 4) == 0:
        print("This year is divisible by 4")

        if(year % 100) == 0:
            print("This year was a century year")
            
            if(year % 400) == 0:
                print("This is a leap year!")
                return(29)
            else:
                print("This is a century year, but not a leap year")
                return(28)
        else:
            print("This is a leap year")
            return(29)
    else:
        print("This is not a leap year")
        return(28)
    print()
    
#------------------------------------------------------------------------#

    

#----------This function splits the date into seperate peices------------#
    
def splitDateUp(date):
    splitDate = date.split("/")
    return(splitDate)

#------------------------------------------------------------------------#



#------------------Start function dateValidation-------------------------#
    #This function validates the day of the month by compairing it to the
    #number of days that are in each month, excpt for FEB, for Feb it
    #calls the leap year funtion, and then returns the correct number of
    #Days for that month determined by the year entered. This function
    #will return a valid message to the user or an invalid date message
    

def dateValidation(month, day, year):
    if month <= 12 and month >= 1:
        print("This is a valid month")
    else:
        print("you typed an invalid month")

    
    if day >= 1 and day <=31:
       if month == 1:
           if day <=31:
               print("This is a valid day in Jan")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 2:
           if day <= leapYear(year):
                print("This is a valid day in Feb")
                return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 3:
           if day <=31:
               print("This is a valid day in Mar")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 4:
           if day <=30:
               print("This is a valid day in Apr")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 5:
           if day <=31:
               print("This is a valid day in May")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 6:
           if day <=30:
               print("This is a valid day in Jun")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 7:
           if day <=31:
               print("This is a valid day in Jul")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 8:
           if day <=31:
               print("This is a valid day in Aug")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 9:
           if day <=30:
               print("This is a valid day in Sept")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 10:
           if day <=31:
               print("This is a valid day in Oct")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 11:
           if day <=30:
               print("This is a valid day in Nov")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
       if month == 12:
           if day <=31:
               print("This is a valid day in Dec")
               return("THIS DATE IS VALID")
           else:
               return("This date is not valid")
    else:
        return("Not a valid Day of the month")

        
#-------------------------------------------------------------------------#


#---------------------------MAIN FUNCTION---------------------------------#
def main():
    date = input("Enter a date in the form of month/day/year 9/24/2020: ")

    splitDate = splitDateUp(date)
    
    print(dateValidation(int(splitDate[0]),int(splitDate[1]),int(splitDate[2])))
    
main()


input("Press <Enter> to quit ")



