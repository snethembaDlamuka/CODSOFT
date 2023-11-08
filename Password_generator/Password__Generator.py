import random
import string


def generate_password(length): 
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    try:
        password_length = int(input("Enter the desired password length: "))

        if password_length <= 0:
            print("Password length should be a positive integer.")
        else:
            generated_password = generate_password(password_length)
            print("Generated password: ", generated_password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")







if __name__=="__main__":
    main()                  