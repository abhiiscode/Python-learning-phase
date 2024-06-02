files = open("essay.txt", 'r')
content = files.read()
# files.readlines()
converted_text = content.title()

# for file in files:
#     content = file.title()
#
print(converted_text)