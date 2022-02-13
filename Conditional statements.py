# conditional statements
pears = 11
papaya = 19
print(pears < papaya)

hungry = True
coworkers_going = False
brought_lunch = False

#We want to print True if hungry is True and if either
#brought_lunch is False or coworkers_going is True. How do
#we build this? Let's take it piece by piece.
#
#First, if hungry is False, then we'll always print False.
#That means that hungry must be part of an 'and' statement.
#So, for starters, we know our line will say something like
#print(hungry and ...)
#
#What about the second part? Notice that it says *either*.
#'either' means 'or'. So, we know the remainder of our
#statement is going to be an 'or'. We also know it should be
#in parentheses because 'hungry' is part of an 'and'
#statement with this entire 'or' statement, not just the
#first part.
#
#So, now we have:
#print(hungry and (... or ...))
#
#Now, finally, we can fill in those two blanks. Our 'either'
#is between coworkers_going being True and brought_lunch
#being False. So, our final statement is:

#print(hungry and (coworkers_going or not brought_lunch))
#print((coworkers_going or not brought_lunch)and hungry)
#The 'not' in front of brought_lunch turns it True in this
#statement if its value is False, which is what we want.


