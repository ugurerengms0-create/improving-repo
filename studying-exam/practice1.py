urunler = []
fiyatlar = []

for i in range(3):
    urun = input("Ürünün adını girin: ")
    i = i+1
    while True:
        fiyat = float(input("ürünün fiyatını girin: "))
        if fiyat < 0:
            print("Fiyat negatif olamaz. Lütfen geçerli bir fiyat girin.")
        else:
            break

    urunler.append(urun)
    fiyatlar.append(fiyat)

print("\nÜrünler ve Fiyatları:")
print("-" * 30)
for i in range(len(urunler)):
    print(f"{urunler[i]}: {fiyatlar[i]} TRY")
print(f"Toplam Fiyat: {sum(fiyatlar)} TRY")
print(f"Ortalama Fiyat: {sum(fiyatlar)/len(fiyatlar):.2f} TRY")
print(f"En Düşük Fiyat: {min(fiyatlar)} TRY")
print(f"En Yüksek Fiyat: {max(fiyatlar)} TRY")