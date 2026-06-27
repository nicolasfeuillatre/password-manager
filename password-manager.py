""" Password Manager - see README for details """

import hashlib #Secure hashes and message digests
import getpass #Portable password input

password_manager = {}

def create_account():
    username = input("Enter your username : ")
    password = getpass.getpass("Enter your password : ") #Works like an input, but hide the characters on screen
    hashed_password = hashlib.sha256(password.encode()).hexdigest() #.encode converts your string into bytes,
    # then hashlib.sha256 runs the SHA-256 algorithm, and finally .hexdigest() converts it into a readable string
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username : ")
    password = getpass.getpass("Enter your password : ") 
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()