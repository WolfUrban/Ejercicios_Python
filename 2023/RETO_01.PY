leet_alphabet = {
    'A': '4',
    'B': '8',
    'C': '(',
    'D': '|)',
    'E': '3',
    'F': '|=',
    'G': '6',
    'H': '#',
    'I': '1',
    'J': '_|',
    'K': '|<',
    'L': '|_',
    'M': '|\/|',
    'N': '|\|',
    'O': '0',
    'P': '|*',
    'Q': '(_,)',
    'R': '|2',
    'S': '5',
    'T': '7',
    'U': '|_|',
    'V': '\/',
    'W': '\/\/',
    'X': '><',
    'Y': '`/',
    'Z': '2',
    '0': 'O',
    '1': 'I',
    '2': 'Z',
    '3': 'E',
    '4': 'A',
    '5': 'S',
    '6': 'G',
    '7': 'T',
    '8': 'B',
    '9': 'P'
}

text_hacker =""
text = input("Ingrese palabra: ").upper()

for t in text:
    
    if t in leet_alphabet:
        text_hacker += leet_alphabet[t]
    else:
        text_hacker += t

print(text_hacker)
