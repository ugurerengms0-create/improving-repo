# Week 1, 3 (Loops) ve Week 4 (Functions) Entegrasyonu

def hesapla_butce(gunluk_para):
    """Günlük parayı alarak haftalık, aylık ve yıllık bütçeyi hesaplar."""
    weekly = gunluk_para * 7
    monthly = gunluk_para * 30
    yearly = gunluk_para * 365
    return weekly, monthly, yearly

def butce_analizi_yap(yillik_butce):
    """Yıllık bütçeye göre durumu ekrana yazdırır."""
    print("-" * 30)
    print("Bütçe Analizi")
    if yillik_butce >= 100000:
        print("Durum: Lüks Sınıf 🚀 (Yıllık bütçen gayet yüksek!)")
    elif 50000 <= yillik_butce < 100000:
        print("Durum: Orta Sınıf 🚗 (Yıllık bütçen orta seviyede.)")
    else:
        print("Durum: Fakir Sınıf 🐻 (Yıllık bütçen düşük.)")

# --- ANA PROGRAM AKIŞI ---

name = input("Enter your name: ").capitalize().strip()

while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        else:
            break
    except ValueError:
        print("Geçersiz değer! Lütfen tam sayı girin.")

while True:
    try:
        money = float(input("Enter your daily money: "))
        if money < 0:
            print("Money cannot be negative. Please enter a valid amount.")
        else:
            break
    except ValueError:
        print("Geçersiz değer! Lütfen sayısal bir ifade girin.")

# Fonksiyonu çağırarak değerleri hesaplatıyoruz
weekly_money, monthly_money, yearly_money = hesapla_butce(money)

# Çıktı Raporu
print(f"\nHello {name}. Your informations are showed in the table.")
print("-*" * 30)
print(f"Name: {name}")
print(f"Age: {age}")
print(f"\nWeekly Money: {weekly_money:.2f} TRY")
print(f"Monthly Money: {monthly_money:.2f} TRY")
print(f"Yearly Money: {yearly_money:.2f} TRY")

# Analiz fonksiyonunu çağırıyoruz
butce_analizi_yap(yearly_money)