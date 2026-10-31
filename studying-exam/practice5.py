bakiye = 1000

def bakiye_sorgula(bakiye):
    print(f"Bakiyeniz: {bakiye}")

def para_yatir(bakiye):
    while True:
        yatiralacak = float(input("Yatıracağınız miktarı giriniz (pozitif)"))
        if yatiralacak < 0:
            print("Yatırılacak tutar pozitif olmalıdır!")
        else:
            bakiye += yatiralacak
            print(f"✅ İşlem başarılı! Yeni bakiyeniz: {bakiye:.2f} TRY")
            return bakiye

def para_cek(bakiye):
    while True: 
        cekilecek = float(input("Çekmek istediğiniz tutarı giriniz:"))
        if cekilecek > bakiye:
            print("Yetersiz bakiye!")
        elif cekilecek < 0:
            print("Negatif tutar. Tekrar deneyiniz.")
        else:
            bakiye -= cekilecek
            print(f"✅ İşlem başarılı! Kalan bakiye: {bakiye:.2f} TRY")
            return bakiye

while True:
    ana_soru = input("Yapmak istediğiniz işlemi girin \n(Bakiye sorgulamak için 1, \nPara yatırmak için 2, \nPara çekmek için 3, \nÇıkış yapmak için q tuşuna basınız):")
    if ana_soru == '1':
        bakiye_sorgula(bakiye)
    elif ana_soru == '2':
        bakiye = para_yatir(bakiye)
    elif ana_soru == '3':
        bakiye = para_cek(bakiye)
    elif ana_soru == 'q':
        print(f"Son bakiye: {bakiye:.2f} TRY \nÇıkış yapılıyor...")
        break












  
    