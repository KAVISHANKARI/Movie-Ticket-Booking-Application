import functions
def getAdminCredentials():
    username=input("Enter username:")
    password=input("Enter password:")
    return username,password
def adminDashBoard():
    while True:
        print("---------------------------------------------------------------------------------")
        print("|                                Admin Dashboard                                |")
        print("---------------------------------------------------------------------------------")
        print("1)Add movie\n2)Add theatre\n3)View bookings\n4)Exit")
        inp=int(input())
        if inp==1:
            movie_name=input("Enter movie name:")
            movie_theatre=input("Enter theatre name:")
            show_date=input("Enter show date:")
            if functions.addMovie(movie_name,movie_theatre,date):
                print("Movie added successfully!!")
            else:
                print("Oops!Problem with server.Try again later..!")
            print("---------------------------------------------------------------------------------")
        elif inp==2:
            movie_name=input("Enter movie name:")
            movie_theatre=input("Enter theatre name:")
            show_date=input("Enter show date:")
            if functions.addMovie(movie_name,movie_theatre,show_date):
                print("Theatre added successfully!!")
            else:
                print("Oops!Problem with server.Try again later..!")
            print("---------------------------------------------------------------------------------")
        elif inp==3:
                functions.viewBooking()
        else:
            break