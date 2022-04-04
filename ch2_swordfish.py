while True:
    print('Who are you?')
    name = input()
    if name != 'Carr':
        print('Wrong name.')
        continue
    else:
        break
print ('Hello, Carr. What is the password? (It is a fish.)')
while True:
    password = input()
    if password != 'swordfish':
        print('Wrong password. Try again.')
        continue
    else:
        break
print('Access granted.')
