stok_sistemi = {}

for i in range(3):
    key = input("Ürünün adını girin: ").lower().strip()
    while True:
        value = float(input("Ürünün fiyatını girin: "))
        if value < 0:
            print("Fiyat negatif olamaz. Lütfen geçerli bir fiyat girin.")
        else:
            break
    stok_sistemi[key] = value
while True:
    istek = input("Fiyatını öğrenmek istediğiniz ürünün adını girin(Çıkmak için 'q' tuşuna basın): ").lower().strip()
    if istek == "q":
            print("Programdan çıkılıyor...")
            break
    if istek in stok_sistemi:
        print(f"{istek.capitalize()} ürününün fiyatı: {stok_sistemi[istek]} TRY")
    else:
        print("Ürün bulunamadı.")