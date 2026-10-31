#fonksiyon olusturma
def ortalama_hesapla(vize, final):
    ortalama = (vize * 0.4) + (final * 0.6)
    return ortalama

def harf_notu_hesapla(ortalama):
    if ortalama >= 85:
        return "AA"
    elif ortalama >= 70 and ortalama < 85:
        return "BB"
    elif ortalama >= 50 and ortalama < 70:
        return "CC"
    elif ortalama < 50:
        return "FF Kaldınız."
isim = input("Adınızı girin: ").capitalize().strip()
while True:
    vize = float(input("Vize notunuzu girin: "))
    if vize < 0 or vize > 100:
        print("Geçersiz bir vize notu girdiniz. Lütfen 0 ile 100 arasında bir değer girin.")
    else:
        break
while True:
    final = float(input("Final notunuzu girin: "))
    if final < 0 or final > 100:
        print("Geçersiz bir final notu girdiniz. Lütfen 0 ile 100 arasında bir değer girin.")
    else:
        break

ortalama = ortalama_hesapla(vize, final)
harf_notu = harf_notu_hesapla(ortalama)
print("\n--- ÖĞRENCİ SONUÇ RAPORU ---")
print(f"Merhaba {isim}!")
print(f"Ortalamanız: {ortalama:.2f}")
print(f"Harf Notunuz: {harf_notu}")