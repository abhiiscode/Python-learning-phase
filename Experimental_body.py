import glob
myfile = glob.glob("*.txt")
print(myfile)

for i in myfile:
    with open(i, 'r') as file:
        print(file.read().upper())

#
# for i in myfile:
#     with open(i, 'r') as file:
#         print(file.readlines())
