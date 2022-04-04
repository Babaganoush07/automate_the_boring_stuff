def is_phone_number(text):
    if len(text) != 12:
        return False
    for item in range(0,3):
        if not text[item].isdecimal():
            return False
    if text[3] != '-':
        return False
    for item in range(4, 7):
        if not text[item].isdecimal():
            return False
    if text[7] != '-':
        return False
    for item in range(8, 12):
        if not text[item].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(is_phone_number('415-555-4242'))
print('(415) 555-4242 is a phone number:')
print(is_phone_number('(415) 555-4242'))
print('Moshi moshi is a phone number:')
print(is_phone_number('Moshi moshi'))

print()
print('You would have to add even more code to find this pattern of text in a larger string.')

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
print(message)

for item in range(len(message)):
    chunk = message[item:item+12]
    if is_phone_number(chunk):
        print('Phone number found: ' + chunk)
