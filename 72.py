file = open('72a.py')
while True:
    text = file.readline()
    if len(text) == 0:
        break
    elif not text.startswith('#'):
        print(text)
file.close()        
