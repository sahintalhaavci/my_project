#Islem Yapmak Icin
from cal import islemler
soru = input('Baslatmak Istiyor Musunuz? (Evet / Hayir):').lower()

if soru == 'evet':
    def code():
        global x
        global y
        soru2 = input('Islem Seciniz (Toplama,Cikarma,Carpma,Bolme): ').lower()
        try:
            x = int(input('Ilk Sayiyi Giriniz : '))
            y = int(input('Ikinci Sayiyi Giriniz : '))
        except ValueError:
            print('Lutfen Sadece Sayi Giriniz! ')
        if soru2 == 'toplama':
            islemler.toplama(x,y)
        elif soru2 == 'cikarma':
            islemler.cikarma(x,y)
        elif soru2 == 'carpma':
            islemler.carpma(x,y)
        elif soru2 == 'bolme':
            islemler.bolme(x,y)
    code()

    while True:
        soru3 = input('Devam Etmek Istiyor Musunuz (Evet/Hayir): ').lower()
        if soru3 == 'evet':
            code()
        elif soru3 == 'hayir':
            print('Gorusmek Uzere...')
            break
        else:
            print('HATA TEKRAR DENEYIN')
            break
