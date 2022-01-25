def input_message():
    print('Enter the encrypted Caesar cipher message to hack')
    return input('> ')

# MEET ME BY THE ROSE BUSHES TONIGHT
# NFFU NF CZ UIF SPTF CVTIFT UPOJHIU

def hack_it(text: str):
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for key in range(len(symbols)):
        new_message = ''
        for symbol in text:
            if symbol in symbols:
                num = symbols.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(symbols)
                new_message += symbols[num]
            else:
                new_message += symbol
        print(f'Key[{key}] - {new_message}')


if __name__ == '__main__':
    message = input_message()
    hack_it(message)

