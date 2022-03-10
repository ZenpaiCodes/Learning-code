# get user input
user = input("Enter your username: ")
keep_asking = True

while keep_asking:
    password = input("Enter your password: ")
    if len(password) < 15:
        print("password must be at least 15 characters")
    else:
        print("Your password is secure!")
        keep_asking = False