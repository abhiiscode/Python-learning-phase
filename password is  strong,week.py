password = input('Enter a password : ')
result = {}

if len(password) >= 8:
    result["Length"] = True   #("Strong Password")
# elif len(password) < 8:
#     result.append("simple passwrd")
else:
    result["Length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)
print(result.values())

if (all(result.values())):  # in this program .Values() is very IMP because it will check all boolean data type
    print("Strong Password")
else:
    print("Week password")