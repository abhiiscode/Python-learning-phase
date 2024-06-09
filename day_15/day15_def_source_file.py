FILEPATH = 'rows.txt' #'../rows.txt'

def get_todos(filepath=FILEPATH):  # it's only work when we call function (get_todos()) in new variable like : todos = get_todos()
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg, filepath=FILEPATH):  #filepath, todos_arg is the local variable/Parameters
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)