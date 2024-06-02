import webbrowser

user_input = input("Enter what You Want To Search : ").replace(" ", "+")
webbrowser.open("http://www.google.com/search?q=" + user_input)