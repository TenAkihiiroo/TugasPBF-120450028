# Author: Hafizul Damar Laya
# NIM: 120450028
# Affiliation: Sains Data ITERA
# Date: 13 March 2022
# Program Description: Program to solve simple encryption password problem
import speetools_120450028 as tools

lim = 100
p ={'a':26,'c':80}
sandies = []

question = input("Do you want to encrypt passwords? [Y/N] ")
if question == "Y":
    data = int(input("Please enter the number to encrypt passwords: "))
    i = 1
    while i<=data:
        sandie = input('Enter your password: ')
        sandies.append( [sandie, tools.enkripted( sandie, p ) if tools.check_pj(sandie,lim) else 'invalid password'] )
        i = i + 1
    tools.show_password(sandies)
else:
    print("Thank you for using the program")


