correct_username = "Goat"
correct_password = "Gomes"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == correct_username and password == correct_password:
    print(f"Welcome to Tõka, {username} {password}!")
else:
    print(f"Access denied! Go away, {username}!")
    