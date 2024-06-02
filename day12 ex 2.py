password = input("Enter a password : ")


def strength(password):
    strength = {}
    if len(password) >= 8:
        strength["length"] = True
    else:
        strength["length"] = False

    # result["length"] = result
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    strength["digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase = True
    strength["uppercase"] = uppercase

    print(strength.values())

    if all(strength.values()):
        print("Strong password")
    else:
        print("weak password")
        return strength
a = (strength(password))
print(a)






