def CaesarCipherChar(c, k):
    if 'A' <= c <= 'Z': #если заглавная
        if ord(c) + 3 > 90: #больше ли номер буквы последнего номера алфавита
            return chr(ord(c) + k - 26)
        else:
            return chr(ord(c) + k)
    elif 'a' <= c <= 'z': #если маленькая
        if ord(c) + 3 > 122: #больше ли номер буквы последнего номера алфавита
            return chr(ord(c) + k - 26)
        else:
            return chr(ord(c) + k)
    else: #обычный символ(можно без else, но так тебе будет понятнее)
        return c
def CaesarCipher(s, k):
    ans = ''
    #цикл для чтения каждого символа
    for i in range(len(s)):
        c = s[i]
        #вызываем функцию, возвращающую зашифрованную букву
        ans += CaesarCipherChar(c, k)
    return ans
S = input()
print(CaesarCipher(S, 3))