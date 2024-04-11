import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(random.choice(characters) for _ in range(length))
    return passw

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a valid positive integer for the length.")
            return
        passw = generate_password(length)
        print("Generated password:", passw)
    except ValueError:
        print("Please enter a valid positive integer for the length.")

if __name__ == "__main__":
    main()
