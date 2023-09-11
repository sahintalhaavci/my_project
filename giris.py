#Login Sistemi
#Kodu Lutfen Ellemeyin!!
global login
global kayit
print('Islem Seciniz ..')
db = {'123':'123'}
soru = input('\tKayit \n\tGiris \nIslem Giriniz : ').lower()
def kayit():
    global k_sifre
    global k_log
    global k2_sifre
    k_log = str(input('Login Giriniz : '))
    k_sifre = str(input('Sifre Giriniz : '))
    k2_sifre = str(input('Sifreyi Tekrarlayninz :'))
    if len(k_sifre) < 8:
        print('Sifre 8 Sembolden Olusmali Tekrar Deneyiniz! ')
    elif k_sifre == k2_sifre:
        db[k_log] = k_sifre
        print(f'Kayit Tamamlandi .. \n \t Login :{k_log}  \n\t Sifreniz :{k_sifre} \n\tLogin Sayfasina Yonlendirliyorsunuz')
    elif k_sifre != k2_sifre and len(k_sifre) < 8:
        print('Yanlis Sifre')
        kayit()
def login():
    global a
    for k,v in db.items():
        login = str(input('Login Giriniz : '))
        sifre = str(input('Sifre Giriniz : '))    
        if k == login and v == sifre:
            print('Giris Yapildi')
            return True
        elif k != login and v != sifre:
            print('Hatali Login Tekrar Deneyiniz')
            print('Hatali Sifre Tekrar Deneyiniz')
            break

if soru == 'kayit':
    kayit()
    soru2 = input('Giris Yapmak Istiyor Musunuz(Evet /Hayir)').lower()
    if soru2 == 'evet':
        login()
        a = 1
    else:
        print('Misafir Olarak Devam Ediliyor...')

elif soru == 'login':
    login()