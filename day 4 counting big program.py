todos = []
# file = open(r"C:\Users\Abhi\PycharmProjects\pythonProject\row.txt", 'r') we use "r" for removing \n, \t, \a effect in location path

while True:
    user_action = input("add, show, edit, remove/complete, all items, or exit : ")
    user_action = user_action.strip() # use : remove space from input(user_action)

    match user_action:
       case 'add' | 'ADD' | 'Add':
           todo = input("Enter what you want : ") + '\n'

           # file = open('row.txt', 'r')
           # todos = file.readlines()         # method 1 (dump method)
           # file.close() # its imp to close file because other can't modified your file

           with open('row.txt', 'r') as file:
               todos = file.readlines() #   method 2

           todos.append(todo)

           file = open('row.txt', 'w')
           file.writelines(todos) # it will posible in it: file.writelines(['a', 'b', 'c'])
           file.close()

       case 'show' | 'SHOW' | 'Show':
           with open('row.txt', 'r') as file:
               todos = file.readlines()

           # new_todos = []
           # for item in todos:
           #     new_item = item.strip('\n')
           #     new_todos.append(new_item)   # method 1 :for strip ("\n")
           #
           # todos = [item.strip('\n') for item in todos]   # method 2 :for strip ("\n")

           for index, item in enumerate(todos):
               item = item.strip("\n") # use : to remove ("\n") | # method 3 :for strip ("\n")
               index = index + 1
               second_trick = f"{index}-{item}" #as well as we can write {index + 1} for start index from 1
               # print(index, item)
               print(second_trick)

               file = open('row.txt', 'w')
               file.writelines(todos)  # it will posible in it: file.writelines(['a', 'b', 'c'])
               file.close()

       case 'edit' | 'EDIT' | 'Edit':
           number = int(input("Enter number which you want to change : "))

           with open('row.txt', 'r') as file:
               todos = file.readlines()

           number = number - 1
           print('You choose this word to Edit : ', todos[number])
           new_char = input("Enter new charecter : ")
           todos[number] = new_char + '\n'
           # number = number + 1
           print(number + 1,'replaced by : ',new_char) #in loop we can print index one by one with out using [number = number + 1]

           with open('row.txt', 'w') as file:
               file.writelines(todos)  # it will posible in it: file.writelines(['a', 'b', 'c'])

           # for item in todos:
           #     print(item)
       case 'complete' | 'COMPLETE' | 'Complete' | 'Remove' | 'REMOVE' | 'remove':
           number = int(input("Enter number which you want to remove : "))
           number = number - 1
           user_remove_item =  todos[number].strip('\n')
           todos.pop(number)

           with open('row.txt', 'w') as file:
               file.writelines(todos)

           message = f"You remove {user_remove_item} form the list."
           print(message)

       case 'all items':
           print(len(todos))
       case 'exit' | 'EXIT' | 'Exit':

           break
       case whatever:  # most of programer use _ for whatever   "_"


           print("hey you enter a unknown command here please try again")

print("thanx for intracting with us !")

