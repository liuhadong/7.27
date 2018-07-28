file = open('73a.py')
text = file.read()
list = []
for i in text.split(','):
    list.append(int(i))
list.sort()
print(list)
