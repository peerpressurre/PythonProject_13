def pali():
    try:
        text = input('Enter your text->')
        res = text.count('.') + text.count('!') + text.count('?')
        print(f'The number of sentences:{res}')
    except Exception as ex:
        print(f'Error: {ex}')
pali()