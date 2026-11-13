import time
import getpass
USERNAME = "admin"
PASSWORD = "Cyber123"

MAX_ATTEMPTS = 3
LOCK_TIME = 30

def login_system():
    attempts = 0

    print("===== LOGIN ATTEMPT CONTROL SYSTEM =====")

    while attempts < MAX_ATTEMPTS:

        username = input("\nEnter username: ")
        password = getpass.getpass("Enter password: ")

        if username == USERNAME and password == PASSWORD:
            print("\nLogin successful! Welcome.")
            return

        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts

            print("\nIncorrect username or password!")

            if remaining > 0:
                print("Attempts remaining:", remaining)

    print("\nToo many failed attempts!")
    print("Account temporarily locked.")

    time.sleep(LOCK_TIME)

    print("\nLock period completed. You can try again.")

    login_system()

login_system()
