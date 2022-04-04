import pyperclip

text = pyperclip.paste()

for char in '-.,\n':
    text=text.replace(char,' ')
text = text.lower().split()

d = {}

for word in text: 
    d[word] = d.get(word, 0) + 1

print('Words used: \n')

for k in sorted(d, key=d.get, reverse=True):
    print(k, ':', d[k])

print('Total words used: '+str(len(d)))
    
while True:
    search = str(input("SEARCH: "))
    if search in d:
        print(search+': '+str(d[search]))
    else:
        print(search + ' Not found')

input('\n Press any key to exit')
