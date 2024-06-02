# password = input("Enter a password : ")
#
# result = {}
#
# if len(password) >= 7:
#     result["Great password there"] = True
# elif len(password) == 7:
#     result["Password is OK, but not too strong"] =
# else:
#     result = ["Your password is weak"]
#
# print(f"{result}")


# ??????????????????????????????????????????????????????????????

# day_temperatures = {}
#
# day_temperatures["morning"] = (22.22, 1.1, 2.2)
# day_temperatures["noon"] = (1.22, 44.66, 45.66)
# day_temperatures["evening"] = (2.22, 22.43, 32.32)
#
# print(day_temperatures)

# ??????????????????????????????????????????????????????????????

def go_green():
    ju = "abhi"
    # prem = "dd"
    new_ju = ju.title()
    print("ju")
    return new_ju

abhi = go_green()
print(abhi)




# print(f"{result}")


# import re  # Import the regular expressions module
#
#
# def check_password_strength(password):
#     # Check if the password is less than 8 characters
#     if len(password) < 8:
#         return "Simple"
#
#     # Check for diversity in characters using regular expressions
#     has_upper = bool(re.search(r'[A-Z]', password))  # Check for uppercase letters
#     has_lower = bool(re.search(r'[a-z]', password))  # Check for lowercase letters
#     has_digit = bool(re.search(r'\d', password))  # Check for digits
#     has_special = bool(re.search(r'[\W_]', password))  # Check for special characters
#
#     # Strong: At least 8 characters and has a mix of all character types
#     if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
#         return "Strong"
#
#     # Weak: At least 8 characters but lacks character diversity
#     return "Weak"
#
#
# # Get password input from the user
# user_password = input("Enter your password: ")
#
# # Check the strength of the entered password
# password_strength = check_password_strength(user_password)
#
# # Print the result
# print(f"Password: {user_password}, Strength: {password_strength}")
