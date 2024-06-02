filenames = ['doc.txt', 'report.txt', 'presentation.txt']


for filename in filenames:
    add = "hallo"
    file = open(filename, 'w')
    file.write(add)
    file.close()