def pali():
    try:
        text = input('enter text -')
        text_words = input('enter words -')
        words = text_words.split()
        print(words)
        for word in words:
            if text.count(word)>0:
                orig = word
                new = word.title()

                text = text.replace(orig, new)
        print(text)

    except Exception as ex:
        print(f'Error: {ex}')
pali()