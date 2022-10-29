def pali():
    try:
        text = input('')
        res = text.count('.') + text.count('!') + text.count('?')
    except Exception as ex:
        print(f'Error: {ex}')
pali()