import ibm_db

conn = ibm_db.connect("","", "")
if conn :
    print('connected')
else:
    print("failed to connect")


def createUser(name, user_id,password):
    stmt = "insert into User (name , user_id , password) values ('"+name+"','"+user_id+"','"+password+"');"
    if ibm_db.exec_immediate(conn, stmt):
        return True
    else:
        return False

def loginUser(user_id, password):
    stmt = ibm_db.exec_immediate(conn, "select password from user where user_id='"+user_id+"';")
    entries = 0
    while ibm_db.fetch_row(stmt) != False:
        entries += 1
        value = ibm_db.result(stmt, 0)
        print("Password: ", value)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def adminLogin(username,password):
    stmt=ibm_db.exec_immediate(conn,"select password from ADMIN where username='"+username+"';")
    entries = 0
    while ibm_db.fetch_row(stmt) != False:
        entries += 1
        value = ibm_db.result(stmt, 0)
        DBpassword = value
        if DBpassword != password:
            return False
        else:            
            return True

def createAdmin(username,password):
    stmt = "insert into ADMIN (username,password) values ('"+username+"','"+password+"');"
    if ibm_db.exec_immediate(conn, stmt):
        return True
    else:
        return False

def searchMovieByName(movie_name):
    sql= "select * from cinema where movie_name='"+movie_name+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("--------------------------------------------------------------------------------")
    print("|       Cinema Name           |         Theatre Name          |       Date     |")
    print("--------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:29s}|{:31s}|{:16s}|".format( dictionary[0],dictionary[1],dictionary[2])) 
        print("--------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)

def searchMovieByTheatre(movie_theatre):
    sql= "select * from cinema where movie_theatre='"+movie_theatre+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("--------------------------------------------------------------------------------")
    print("|       Cinema Name           |         Theatre Name          |       Date     |")
    print("--------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:29s}|{:31s}|{:16s}|".format( dictionary[0],dictionary[1],dictionary[2])) 
        print("--------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)

def searchMovieByDate(date):
    sql= "select * from cinema where show_date='"+date+"';"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("--------------------------------------------------------------------------------")
    print("|       Cinema Name           |         Theatre Name          |       Date     |")
    print("--------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:29s}|{:31s}|{:16s}|".format( dictionary[0],dictionary[1],dictionary[2])) 
        print("--------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)

def bookTicket(user_id,movie_name,movie_theatre,show_date,seat):
    stmt = "insert into Booking (user_id,movie_name,movie_theatre,show_date,seat) values ('"+user_id+"','"+movie_name+"','"+movie_theatre+"','"+show_date+"','"+str(seat)+"');"
    if ibm_db.exec_immediate(conn,stmt):
        return True
    else:
        return False

def addMovie(movie_name,movie_theatre,show_date):
    stmt = "insert into Cinema (movie_name,movie_theatre,show_date) values ('"+movie_name+"','"+movie_theatre+"','"+show_date+"';"
    if ibm_db.exec_immediate(conn,stmt):
        return True
    else:
        return False

def viewBooking():
    sql= "select * from booking"
    stmt=ibm_db.exec_immediate(conn,sql)
    dictionary = ibm_db.fetch_both(stmt)
    print("-------------------------------------------------------------------------------------------------")
    print("| Person's Name |       Cinema Name      |     Theatre Name     |      Date      | Seats Booked |")
    print("-------------------------------------------------------------------------------------------------")
    while dictionary != False:
        print("|{:15s}|{:24s}|{:22s}|{:16s}|{:14s}".format( dictionary[0],dictionary[1],dictionary[2],dictionary[3],dictionary[4])) 
        print("-------------------------------------------------------------------------------------------------")
        dictionary = ibm_db.fetch_both(stmt)