import string
import getpass

def check_pw():
    password = getpass.getpass("Enter Your Password: ")
    strength = 0
    remark = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1      
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        remark = "Very Bad Password!!"
    elif strength == 2:
        remark = "Bad Password!!"
    elif strength == 3:
        remark = "Weak Password!!"
    elif strength == 4:
        remark = "Can be a Better Password!!"
    elif strength == 5:
        remark = "Strong Password!!"

    print("\nYour Password Has:")
    print(f"{lower_count} lower case characters")
    print(f"{upper_count} upper case characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")  

    print(f"\nPassword Strength: {strength}")
    print(f"Hint: {remark}")

def ask_to_continue(is_retry=False):
    if is_retry:
        choice = input('\nDo you want to check another password? (y/n): ')
    else:
        choice = input("Do you want to check your Password's Strength? (y/n): ")

    if choice.strip().lower() == 'y':
        print("You chose to continue.")
        return True
    elif choice.strip().lower() == 'n':
        print("You chose to exit. Goodbye!")
        return False
    else:
        print("Invalid input. Exiting by default.")
        return False

if __name__ == '__main__':
    print('Welcome to the Password Strength Checker!')
    while ask_to_continue():
        check_pw()
