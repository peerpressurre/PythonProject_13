def pali():
    try:
        text = input('enter text -')
        text_words = input('enter words -')
        words = text_words.split()
        for word in words:
            if text.count(word)>0:
                orig = word
                new = word[0].upper()+word[1:]

                text = text.replace(orig, new)
        print(text)

    except Exception as ex:
        print(f'Error: {ex}')
pali()
