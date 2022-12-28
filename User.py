from tokenize import Name
from unicodedata import name
import functions
def getUserCredentials():
    username=input("Enter username:")
    password=input("Enter password:")
    return username,password

def createUser():
    name=input("Enter name:")
    username=input("Enter user id:")
    password=input("Enter password:")
    return name,username,password

def userDashBoard(username):
    while True:
        print("---------------------------------------------------------------------------------")
        print("|                                User Dashboard                                 |")
        print("---------------------------------------------------------------------------------")
        print("1)Search\n2)Book\n3)Logout")
        inp=int(input())
        if inp==1:
            print("1)Search by movie name\n2)Search by theatre name\n3)Search by date")
            choice=int(input("Enter your choice:"))
            if choice==1:
                name=input("Enter movie name:")
                functions.searchMovieByName(name)
            elif choice==2:
                theatre=input("Enter theatre name:")
                functions.searchMovieByTheatre(theatre)
            else:
                date=input("Enter date:")
                functions.searchMovieByDate(date)
        elif inp==2:
            name=input("Enter movie name:")
            theatre=input("Enter theatre name:")
            date=input("Enter date:")
            seat=int(input("Enter no.of seats:"))
            if functions.bookTicket(username,name,theatre,date,seat):
                print("Successfully booked!!")
        else:
            break