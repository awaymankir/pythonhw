def word(words):
    str = words.lower().split()
    f = lambda x: sum(1 for i in x if i in 'аоуыэеёиюя')
    tmp = f(str[0])
    if all([f(i) == tmp for i in str]):
        return 'Парам пам-пам'
    return 'Пам парам'


print(word("пара-ра-рам рам-пам-папам па-ра-па-дам "))