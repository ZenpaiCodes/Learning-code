print('''
Welcome to password checker!
let\'s make sure your password is secure.
      ''')

username = input("Please enter your username: ")
keep_asking = True

while keep_asking:
    password = input("Please enter a password with at least 15 characters: ")
    if len(password) < 15:
        print("Password is too short. Provide at least 15 characters.\n")
    else:
        password_length = len(password)
    keep_asking = False

print(f"Awesome! {username} Your password is {password_length} characters long. You have a SECURE password.")
