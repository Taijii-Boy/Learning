# 415-555-4242

def is_phone_number(text: str) -> bool:
    if len(text) != 12:
        return False
    if not text[:3].isdecimal() or not text[4:7].isdecimal() or not text[8:].isdecimal():
        return False
    if text[3] != '-' or text[7] != '-':
        return False
    return True

# print('415-555-4242 - это телефонный номер?')
# print(is_phone_number('415-555-4242'))
# print('Boba Moba - это телефонный номер?')
# print(is_phone_number('Boba Moba'))


message = 'Позвони мне завтра по номеру 415-555-1011. 415-555-9999 - это номер телефона моего офиса.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if is_phone_number(chunk):
        print(f'{chunk} - Это телефонный номер')