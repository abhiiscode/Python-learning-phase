i = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  # -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
print(i[0:5:2])  #list is print from 4 char because char count from 0 (0,1,2,3,4) = 5
 # i[from : to : skip char/ reverse]

print(i[::-1])   #it will reverse the list because -1 is start from last char

print(i[-1:2:-2]) #
# 1)it will start from -1 = last char
# 2)up to 2 = (0,1,2) 3, and
# 3) -2 = - is fist reverse list and 2 is skiping char for 1 then get next char