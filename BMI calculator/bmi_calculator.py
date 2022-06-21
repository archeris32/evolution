import os
from time import sleep

#defining the menu
def menu():
    sleep(1)
    os.system('cls')
    print("\nMENU")
    print("1.Metric")
    print("2.Imperial")
    print("3.Quotes")
    print("Quit")
#define function to calculate BMI in metric system
def metric():
    weight=float(input("Please enter your weight in kg\n"))
    height=float(input("Please enter your height in meters\n"))
    BMI_metric=weight/(height*height)
    print("your BMI in metric system is : " + str(BMI_metric))
    if(BMI_metric>0):
        if(BMI_metric<=16):
            print("You are very underweight")
        elif(BMI_metric<=18.5):
            print("You are underweight")
        elif(BMI_metric<=25):
            print("Congrats! You are Healthy")
        elif(BMI_metric<=30):
            print("You are overweight")
        else: 
            print("You are very overweight/obese")
    else:
        print("impossible!!!!")
#define function to calculate BMI in imperial system
def imperial():
    weight=int(input("Please enter your weight\n"))
    height=float(input("Please enter your height\n"))
    BMI_imperial=(weight/(height*height))*703
    print(name+ ", your BMI in metric system is : " + str(BMI_imperial))
print("\nWelcome to BMI calculator.")
print("\nA simple way to calculate if you have to go to gym or not.")
sleep(2)
os.system('cls')
print("Please enter your name bellow: \n")
name= input()
menu()
choice=input()
while True:
    if choice == '1':
        metric()
        break
    elif choice == '2':
        imperial()
        break
    elif choice in ['q','quit','Quit','4']:
        print("GoodBye " + name)
        exit()
    else:
        print("Sorry , wrong choice, try again")
        menu()
        choice=input()
