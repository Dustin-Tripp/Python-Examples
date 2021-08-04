# NAME:     Dustin Tripp
# DATE:     09/14/2020
# FILE:     futureDustinTripp.py
# PURPOSE:  A program that calculates future values
from graphics import *
def main():

    #------------ADDED CODE------------------#
    # Creating a window for inputs
    winA = GraphWin("Inputs: ", 400,400)

    # Drawing input questions
    Text(Point(100,30), "Enter the initial principal : ").draw(winA)
    Text(Point(123,70), "Enter the annalized intrest rate : ").draw(winA)

    # Text boxes for users to type answers
    inputPrinc = Entry(Point(230,30), 4)
    inputPrinc.draw(winA)
    inputInt = Entry(Point(275,70), 4)
    inputInt.draw(winA)

    # A place to click for the program to continue
    button = Text(Point(200,200),"Click here to Show Graph")
    button.draw(winA)
    winA.getMouse()

    # Assigning user input to values to be calculated
    principal = float(inputPrinc.getText())
    apr = float(inputInt.getText())

    #-----------END ADDED CODE------------------#
    
    # Introduction
    print("This program plots the growth of a 10-year investment . ")
    # Get principal and interest rate
    #principal = float(input("Enter the initial principal : "))
    #apr = float(input("Enter the annualized interest rate : "))
    # Create a graphics window with labels on left edge
    win = GraphWin(" Investment Growth Chart ", 320, 240)
    win.setBackground("white")
    Text(Point(20, 230), ' O . OK').draw(win)
    Text(Point(20, 180), ' 2 . 5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7 . 5K').draw(win)
    Text(Point(20, 30), '10 . 0K').draw(win)
    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230 - height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for successive years
    for year in range(1, 11):
        # calculate value for the next year
        principal = principal * (1 + apr)
        # draw bar for this value
        xll = year * 25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(xll, 230), Point(xll + 25, 230 - height))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("Press <Enter> to quit ")
    win.close()

main()
