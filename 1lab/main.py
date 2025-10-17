from statistics import *

stroka = input('Введите строку символов только на английском или только на русском без лишних символов, по типу запятых и точек: ')
def checkt(s):
    s= s.replace(' ', '')
    if s.isascii():
        return True
    for char in s:
        if not ('А' <= char <= 'Я' or 'а' <= char <= 'я'):
            return False
    return True

def is_only_letters(s1):
    s1 = s1.replace(' ', '')
    return s1.isalpha()

while checkt(stroka) == False or is_only_letters(stroka) == False:
    stroka = input('Введите строку корректно условию: ')

stroka = stroka.lower()
s2 = stroka.replace(' ', '')
masiv_word = [stroka for stroka in stroka.split()]
masiv_letter = [x for x in s2]
print('Самое частое слово в строке: ', mode(masiv_word))
print('Самая частая буква в строке: ', mode(masiv_letter))
