correct_password = "python123"

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful!")
        break

    attempts = attempts + 1

    remaining = max_attempts - attempts

    if remaining > 0:
        print("Incorrect password.")
        print("Attempts remaining:", remaining)
    else:
        print("Account locked.")