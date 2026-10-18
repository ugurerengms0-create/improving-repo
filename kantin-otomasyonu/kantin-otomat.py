import json
from datetime import datetime

menu =  {
    "Tost": 60.0,
    "Sandviç": 50.0,
    "Kahve": 40.0,
    "Çay": 15.0,
    "Su": 10.0,
    "Simit": 20.0,
}
def display_menu():
    print("\n--- Kantin Otomasyonu Menü ---")
    for item, price in menu.items():
        print(f"{item}: {price} TL")
    print("-" * 40)
    
def kasa_guncelle(order, odenen_tutar):
    dosya_adi = "kasa_gecmisi.json"
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    yeni_kayit = {
        "tarih": zaman,
        "siparis": order,
        "odenen_tutar": odenen_tutar
    }

    try:
        with open(dosya_adi, "r", encoding="utf-8") as f:
            veri = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        veri = []   
    veri.append(yeni_kayit)
    with open(dosya_adi, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)
    print("💾 Sipariş kasa geçmişine (kasa_gecmisi.json) başarıyla eklendi.")


def fisi_yazdir(order, total, cut_price=None):
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("siparis_fisi.txt", "w", encoding="utf-8") as f:
        f.write("========================================\n")
        f.write("    İZMİR DEMOKRASİ ÜNİVERSİTESİ KANTİNİ\n")
        f.write(f"    Tarih/Saat: {zaman}\n")
        f.write("========================================\n\n")
        f.write("--- SİPARİŞ DETAYLARI ---\n")
        
        for item, quantity in order.items():
            birim_fiyat = menu[item]
            urun_toplam = birim_fiyat * quantity
            f.write(f"{item} x {quantity} Adet = {urun_toplam:.2f} TL\n")
            
        f.write("----------------------------------------\n")
        f.write(f"Ara Toplam: {total:.2f} TL\n")
        
        if cut_price:
            f.write(f"İndirimli Ödenecek Tutar: {cut_price:.2f} TL\n")
        else:
            f.write(f"Ödenecek Tutar: {total:.2f} TL\n")
            
        f.write("\nBizi tercih ettiğiniz için teşekkür ederiz!\n")
        f.write("========================================\n")
        
    print("\n📄 Sipariş fişiniz 'siparis_fisi.txt' dosyasına başarıyla kaydedildi!")

def calculate_total(order):
    total = 0
    print("--- Sipariş Özeti ---")

    for item, quantity in order.items():
        birim_fiyat = menu[item]
        urun_total = birim_fiyat * quantity
        total += urun_total
        print(f"{item} x {quantity} Adet = {urun_total} TL")
    print("-" * 30)
    print(f"Ara Toplam: {total} TL")


    #İndirim uygulama
    if total >= 200.0:
        odenen_tutar = total * 0.85  # %15 indirim
        print("🎉 200 TL ve üzeri alışverişe %15 İndirim Uygulandı!")
        print(f"İndirimli Toplam: {odenen_tutar:.2f} TL")
        fisi_yazdir(order, total, odenen_tutar)
        kasa_guncelle(order, odenen_tutar)
    elif total >= 100.0:
        odenen_tutar = total * 0.90  # %10 indirim
        print("🎉 100 TL ve üzeri alışverişe %10 İndirim Uygulandı!")
        print(f"İndirimli Toplam: {odenen_tutar:.2f} TL")
        fisi_yazdir(order, total, odenen_tutar)
        kasa_guncelle(order, odenen_tutar)
    else:
        odenen_tutar = total  # İndirim yoksa ödenen tutar ara toplama eşittir
        print(f"Ödenecek Toplam: {odenen_tutar:.2f} TL (İndirim için en az 100 TL alışveriş yapmalısınız.)")
        fisi_yazdir(order, total)
        kasa_guncelle(order, odenen_tutar)
        
    return total
def main():
    order = {}
    while True:
        display_menu()
        item = input("Sipariş etmek istediğiniz ürünü girin (Çıkmak için 'q' tuşuna basın): ").strip().capitalize()
        if item.lower() == 'q':
            print("Siparişiniz tamamlandı. Teşekkür ederiz!")
            break
        if item not in menu:
            print("Geçersiz ürün. Lütfen menüden bir ürün seçin.")
            continue
        try:
            quantity = int(input(f"{item} için adet sayısını girin: "))
            if quantity <= 0:
                print("Adet sayısı pozitif bir sayı olmalıdır.")
                continue
        except ValueError:
            print("❌ Hatalı giriş! Lütfen geçerli bir sayı girin.")
            continue

        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
        print(f"✅ {quantity} adet {item} siparişinize eklendi.")

    if order:
        calculate_total(order)
    else:
        print("Sepetiniz boş, iyi günler dileriz.")

if __name__ == "__main__":
    main()
