def validate_full_name(name):
    if len(name.strip()) == 0:
        return "You haven't entered anything. Please enter your full name."
    elif len(name.split()) < 2:
        return "You have entered less than 2 names. Please make sure that you have entered your name and surname."
    elif len(name) > 25:
        return "You have entered more than 25 characters. Please make sure that you have only entered your full name."
    else:
        return True

def main():
    full_name = input("Enter your full name: ")
    validation_result = validate_full_name(full_name)
    if validation_result is True:
        print("Thank you for entering your full name.")
    else:
        print(validation_result)

if __name__ == "__main__":
    main()