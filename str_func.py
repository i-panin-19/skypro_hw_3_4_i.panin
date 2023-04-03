"""функция всех заглавных букв"""
def big_abc(string):
    return string.upper()


"""функция первой заглавной буквы в каждом слове"""
def big_first_abc(string):
    return ' '.join(word[0].upper() + word[1:] for word in string.split())

"""функция всех прописных букв"""
def small_abc(string):
    return string.lower()
