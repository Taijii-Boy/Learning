def decode_morse(morse_code):
    morse = {'.-': 'A',
             '-...': 'B',
             '-.-.': 'C',
             '-..': 'D',
             '.': 'E',
             '..-.': 'F',
             '--.': 'G',
             '....': 'H',
             '..': 'I',
             '.---': 'J',
             '-.-': 'K',
             '.-..': 'L',
             '--': 'M',
             '-.': 'N',
             '---': 'O',
             '.--.': 'P',
             '--.-': 'Q',
             '.-.': 'R',
             '...': 'S',
             '-': 'T',
             '..-': 'U',
             '...-': 'V',
             '.--': 'W',
             '-..-': 'X',
             '-.--': 'Y',
             '--..': 'Z',
             '.----': '1',
             '..---': '2',
             '...--': '3',
             '....-': '4',
             '.....': '5',
             '-....': '6',
             '--...': '7',
             '---..': '8',
             '----.': '9',
             '-----': '0',
             }

    words = morse_code.split('   ')
    word_by_letters = [letters.split() for letters in words]
    text = ''
    for letters in word_by_letters:
        for letter in letters:
            text += ''.join(morse[letter])
        text += ' '
    return text


print(decode_morse('.... . -.--   .--- ..- -.. .'))
