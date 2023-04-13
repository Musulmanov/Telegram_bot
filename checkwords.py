from uzwords import words
from difflib import get_close_matches

def checkWords(word, words = words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False #Bunday so'z topilmadi

    if word in matches:
        available = True #mavjud
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'x')
        matches.update(get_close_matches(word, words))
    elif 'x' in word:
        word = word.replace('x', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available':available, 'matches':matches}

# if __name__ == '__main__':
#     print(checkWords("ҳато"))
#     print(checkWords('salom'))


