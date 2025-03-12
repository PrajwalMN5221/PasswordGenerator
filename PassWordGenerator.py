#importing random librarie

import random

#Giving values to a  variable

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,.-"

#Adding all the variables in a one single varible
all=lower+upper+numbers+symbols

#Taking input from the user(How much user want lenght of the PassWord)
length=int(input("Enter length of the PassWord:\n"))

#calling the libarie and joining the variable
password="".join(random.sample(all,length))

#Printinf the PassWord
print(password)
