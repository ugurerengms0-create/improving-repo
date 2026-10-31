menu = {"çay": 15.0, "tost": 60.0, "kahve": 80.0}

def menu_goster():
    print("\n----- Menü -----")
    for urun, fiyat in menu.items():
        print(f"{urun.capitalize()}: {fiyat} TRY")
total = 0.0
tercihler = []
while True:
    secim = input("\nMenüyü görmek için '1', Sipari vermek için 2, çıkmak için 'q' tuşuna basın: ")
    if secim == "1":
        menu_goster()
    elif secim == "2":
        siparis = input("Sipariş vermek istediğiniz ürünün adını girin: ").lower().strip()
        if siparis in menu:
            print(f"{siparis.capitalize()} siparişiniz alındı. Fiyat: {menu[siparis]} TRY")
            tercihler.append(siparis)
            total += menu[siparis]
        else:
            print("Ürün menüde bulunamadı.")
    elif secim == "q":
        print("\n----- Sipariş Özeti -----")
        print(f"Siparişleriniz: {tercihler}")
        print(f"Toplam sipariş tutarı: {total} TRY")
        print("Programdan çıkılıyor...")
        break
