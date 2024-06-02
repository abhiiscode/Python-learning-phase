import csv

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))
# print(data)

names = input("Enter any name i give you birth date (abhi, ju, di) : ")

for name in data:
    if name[0] == names:
        print(name[1])
