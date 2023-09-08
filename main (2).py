#Implemantation of program to find leap year


def leap_yr(n):
   if((n%4==0 and n%100!=0) or n%400==0):
     print("{} is a leap year".format(n))
   else:
     print("{} is not a leap year".format(n))
     
       
n=int(input("Enter the year:"))
yr=leap_yr(n)