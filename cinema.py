import Admin,User,functions
while True:
    print("---------------------------------------------------------------------------------")
    print("|                         Cinema Ticket Booking                                 |")
    print("---------------------------------------------------------------------------------")
    print("Log in as:\n1)Admin\n2)User\n3)Signup as user\n4)Signup as admin\n5)Exit")
    inp=int(input())
    if inp==1:
        username,password=Admin.getAdminCredentials()
        if functions.adminLogin(username,password):
            Admin.adminDashBoard()
        else:
            print("Oops!Problem with server.Try again later..!")
    elif inp==2:
        username,password=User.getUserCredentials()
        if functions.loginUser(username,password):
            User.userDashBoard(username)
        else:
            print("Oops!Problem with server.Try again later..!")
    elif inp==3:
        name,user_id,password=User.createUser()
        if functions.createUser(name,user_id,password):
            print("User created Successfully!!")
        else:
            print("Oops!Problem with server.Try again later..!")
    elif inp==4:
        username,password=Admin.getAdminCredentials()
        if functions.createAdmin(username,password):
            print("Admin created Successfully!!")
        else:
            print("Oops!Problem with server.Try again later..!")
    else:
        break