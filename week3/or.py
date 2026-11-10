correct_username = "Goat"
correct_password = "Gomes"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != correct_username or password != correct_password:
    print(f"Access denied! Go away, {username}!")
else:
    print(f"Welcome to Tõka, {username} {password}!")