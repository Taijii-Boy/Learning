def choose_mode() -> str:
    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        answer = input('> ')
        if answer.lower() == 'e':
            return 'e'
        elif answer.lower() == 'd':
            return 'd'


def create_dict(key: int, symbols: str) -> dict:
    """
    Создает словарь, где ключ - буква алфавита, значение - смещенная на key индексов буква алфавита
    """
    alphabet = {}
    for i in range(len(symbols)):
        sum_ = i + key
        if sum_ <= 25:
            alphabet[symbols[i]] = symbols[key+i]
        else:
            alphabet[symbols[i]] = symbols[key+i-26]
    return alphabet


def encrypt_message(message: str, alphabet: dict) -> str:
    message_list = [word for word in message.split()]
    new_message_list = []
    new_word = ''
    for word in message_list:
        for letter in word:
            if letter.upper() in alphabet:
                new_word += alphabet[letter.upper()]
            else:
                new_word += letter
        new_message_list.append(new_word)
        new_word = ''
    return " ".join(new_message_list)


def decrypt_message(message: str, alphabet: dict) -> str:
    new_alphabet = {v: k for k, v in alphabet.items()} # переворачиваем словарь
    return encrypt_message(message, new_alphabet)


def input_key(symbols: str) -> int:
    while True:
        print(f'Please input the key (0 to {len(symbols)-1}) to use')
        key = input('> ')
        if key.isdecimal() and 0 <= int(key) <= 25:
            return int(key)


def input_message(mode: str):
    mode_text = 'encrypt' if mode == 'e' else 'decrypt'
    print(f'Enter the message to {mode_text}')
    return input('> ')


if __name__ == '__main__':
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    chosen_mode = choose_mode()
    key = input_key(symbols)
    message = input_message(chosen_mode)
    alphabet = create_dict(key, symbols)
    if chosen_mode == 'e':
        print(encrypt_message(message, alphabet))
    else:
        print(decrypt_message(message, alphabet))
