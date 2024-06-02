#
# filenames = ['a.txt', 'b.txt', 'c.txt']
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)


filenames = ['a.txt', 'b.txt', 'c.txt']

for filename in filenames:
    file = open(filename, 'r')
    content = file.read() +'\n'
    print(content)
