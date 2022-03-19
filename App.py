import os
import time
import random

# Color Codes [only applicable to Linux]
# "\033[1;31;40m" - RED
# "\033[1;32;40m" - GREEN
# "\033[1;33;40m" - YELLOW
# "\033[1;34;40m" - BLUE
# "\033[1;35;40m" - MAGENTA
# "\033[1;36;40m" - CYAN

# Clear Screen Module that works on Linux/Windows
def Clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# Collecting Data From the User    
def Airdrop_info_maker():
    Clear()
    TokenName = input("Token Name: ")
    if TokenName == "":
        TokenName = "No Token Name Specified"
    else:
        pass
    IssuerAddress = input("Address: ")
    if IssuerAddress == "":
        IssuerAddress = "No Issuer Address Specified"
    else:
        pass
    AirdropDate = input("Airdrop Date: ")
    if AirdropDate == "":
        AirdropDate = "No Airdrop Date Specified"
    else:
        pass
    Requirement = input("Requirements: ")
    if Requirement == "":
        Requirement = "No Requirement Specified"
    elif Requirement == "Yes":
        Requirement = input("Please Specify: ")
    elif Requirement == "yes":
        Requirement = input("Please Specify: ")
    else:
        pass
    Limit = input("Limit: ")
    if Limit == "":
        Limit = "No Limit Specified"
    else:
        pass
    Clear()
    # Printing out Information
    if TokenName == "No Token Name Specified":
        print("Token Name: " + TokenName)
    else:
        print(TokenName)
    if IssuerAddress == "No Issuer Address Specified":
        print("Address: " + IssuerAddress)
    else:
        print(IssuerAddress)
    print("Airdrop:", AirdropDate)
    print("Limit:", Limit)
    print("Requirement:", Requirement)
    # Menu
    print(" ")
    print("Do you want to make another one? ")
    Question = input("Enter Y/y(repeat), R/r(return), N/n(quit): ")
    if Question == "Y":
        return Airdrop_info_maker()
    if Question == "y":
        return Airdrop_info_maker()
    elif Question == "R":
        return Main()
    elif Question == "r":
        return Main()
    elif Question == "N":
        exit()
    elif Question == "n":
        exit()
    else:
        print("Exiting...")
        time.sleep(1)
        Clear()
        exit()
        
def Random_Password():
    Clear()
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "@#$&()"
    all = lower + upper + number + symbol
    length = 10
    password = "".join(random.sample(all,length))
    print("Password: " + password)
    print(" ")
    print("Do you want to make another one? ")
    Question1 = input("Press Enter to repeat, R/r(return), N/n(quit): ")
    if Question1 == "":
        return Random_Password()
    elif Question1 == "R":
        return Main()
    elif Question1 == "r":
        return Main()
    elif Question1 == "N":
        exit()
    elif Question1 == "n":
        exit()
    else:
        print("Exiting...")
        time.sleep(1)
        Clear()
        exit()

# Menu
def Main():
    Clear()
    print("1.Airdrop info maker")
    print("2.Random Password")
    print("3.Quit")
    print(" ")
    Menu = input("Enter Desired Number: ")
    if Menu == "1":
        Airdrop_info_maker()
    elif Menu == "2":
        Random_Password()
    elif Menu == "3":
        Clear()
        exit()
    elif Menu == "":
        return Main()
    else:
        exit()
        
Main()