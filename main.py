#feature/lab_ex1
def pali():
    try:
        word = input()
        if str(word) == str(word)[::-1]:
            print("Palindrome")
        else:
            print("Not Palindrome")
    except Exception as ex:
        print(f'Error: {ex}')
pali()
