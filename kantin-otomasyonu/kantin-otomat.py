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
        cut_price = total * 0.85 #%15 indirim
        print("🎉 200 TL ve üzeri alışverişe %15 İndirim Uygulandı!")
        print(f"İndirimli Toplam: {cut_price:.2f} TL")
    elif total >= 100.0:
        cut_price = total * 0.90 #%10 indirim
        print("🎉 100 TL ve üzeri alışverişe %10 İndirim Uygulandı!")
        print(f"İndirimli Toplam: {cut_price:.2f} TL")
    else:
        print(f"Ödenecek Toplam: {total:.2f} TL (İndirim için en az 100 TL alışveriş yapmalısınız.)")
    return total
def main():
    order = {}
    while True:
        display_menu()
        item = input("Sipariş etmek istediğiniz ürünü girin (Çıkmak için 'q' tuşuna basın): ").title()
        
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
