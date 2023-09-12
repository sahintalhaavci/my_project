print('Hos Geldiniz')
from random import randint
kelimeler = [
    'elma' , 'hesapla' , 'su' , 'insan' , 'inanclar'
]
toplam =+ len(kelimeler)
rsayi = randint(0,toplam -1)

kelime = kelimeler[rsayi]
ksayi =+ len(kelime)

kelimegiz = ''

for i in range(ksayi):
    kelimegiz = kelimegiz+'*'

if kelime == 'elma':
    print(kelimegiz)
    