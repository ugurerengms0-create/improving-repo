import json
from datetime import datetime


class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        self.fiyat = fiyat

class Sepet:
    def __init__(self):
        self.urunler = {}  

    def urun_ekle(self, urun_adi, adet):
        if urun_adi in self.urunler:
            self.urunler[urun_adi] += adet
        else:
            self.urunler[urun_adi] = adet

    def sepeti_goster(self):
        return self.urunler

class Raporlama:
    def __init__(self, dosya_adi="kasa_gecmisi.json"):
        self.dosya_adi = dosya_adi

    def gun_sonu_raporla(self):
        try:
            with open(self.dosya_adi, "r", encoding="utf-8") as f:
                veriler = json.load(f)
        except FileNotFoundError:
            print("\n⚠️ Bilgi: Henüz kasa geçmişi dosyası ('kasa_gecmisi.json') oluşturulmamış.")
            return
        except json.JSONDecodeError:
            print("\n⚠️ Hata: Kasa geçmişi dosyası ('kasa_gecmisi.json') bozuk veya okunamıyor.")
            return
        except (OSError, TypeError) as e:
            print(f"\n⚠️ Kasa geçmişi dosyası okunurken bir hata oluştu: {e}")
            return

        toplam_ciro = 0
        toplam_siparis = len(veriler)
        en_cok_satanlar = {}

        for kayit in veriler:
            toplam_ciro += kayit.get("odenen_tutar", 0)
            siparisler = kayit.get("siparisler", {})

            for urun, adet in siparisler.items():
                if urun in en_cok_satanlar:
                    en_cok_satanlar[urun] += adet
                else:
                    en_cok_satanlar[urun] = adet
        print("\n"+ "="*40)
        print("📊 İZMİR DEMOKRASİ ÜNİVERSİTESİ - GÜN SONU RAPORU")
        print("="*40)
        print(f"Toplam Sipariş Sayısı: {toplam_siparis}")
        print(f"Toplam Kasa Cirosu: {toplam_ciro:.2f} TL")
        print("-"*40)
        print("📦 Ürün Bazlı Satış Adetleri:")
        if en_cok_satanlar:
            for urun, adet in en_cok_satanlar.items():
                print(f"   - {urun}: {adet} Adet")
        else:
            print("Satış verisi bulunamadı.")
        print("="*40)

class KantinYonetimi:
    def __init__(self):
        self.menu = {
            "Tost": Urun("Tost", 60.0),
            "Sandviç": Urun("Sandviç", 50.0),
            "Kahve": Urun("Kahve", 40.0),
            "Çay": Urun("Çay", 15.0),
            "Su": Urun("Su", 10.0),
            "Simit": Urun("Simit", 20.0),
        }
        self.raporlayici = Raporlama()  # Raporlama sınıfından bir nesne oluşturuyoruz

    def menuyu_goster(self):
        print("\n--- 🏫 İDÜ Kantin Otomasyonu (OOP Versiyon) ---")
        for isim, urun_nesnesi in self.menu.items():
            print(f"{isim}: {urun_nesnesi.fiyat} TL")
        print("-" * 40)

    def fisi_yazdir(self, sepet_objesi, total, cut_price=None):
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open("siparis_fisi.txt", "w", encoding="utf-8") as f:
                f.write("========================================\n")
                f.write("    İZMİR DEMOKRASİ ÜNİVERSİTESİ KANTİNİ\n")
                f.write(f"    Tarih/Saat: {zaman}\n")
                f.write("========================================\n\n")
                f.write("--- SİPARİŞ DETAYLARI ---\n")

                for item, quantity in sepet_objesi.items():
                    birim_fiyat = self.menu[item].fiyat
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
        except OSError:
            print("\n❌ Hata: Fiş dosyası diske yazılamadı (Yetki veya disk alanı sorunu).")
        except TypeError as e:
            print(f"\n❌ Fiş yazdırılırken bir hata oluştu: {e}")

    def kasa_guncelle(self, sepet_objesi, odenen_tutar):
        dosya_adi = "kasa_gecmisi.json"
        zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        yeni_kayit = {
            "tarih": zaman,
            "siparisler": sepet_objesi,
            "odenen_tutar": odenen_tutar
        }
        
        try:
            with open(dosya_adi, "r", encoding="utf-8") as f:
                veri = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            veri = []
            
        veri.append(yeni_kayit)

        try:
            with open(dosya_adi, "w", encoding="utf-8") as f:
                json.dump(veri, f, ensure_ascii=False, indent=4)
            
            print("📊 Sipariş kasa geçmişine (kasa_gecmisi.json) eklendi.")
        except OSError:
            print("\n❌ Hata: Kasa geçmişi dosyası diske yazılamadı (Yetki veya disk alanı sorunu).")

    def hesabi_kes(self, sepet_objesi):
        total = 0
        print("\n--- Sipariş Özeti ---")

        for item, quantity in sepet_objesi.items():
            birim_fiyat = self.menu[item].fiyat
            urun_total = birim_fiyat * quantity
            total += urun_total
            print(f"{item} x {quantity} Adet = {urun_total} TL")
            
        print("-" * 30)
        print(f"Ara Toplam: {total} TL")

        # İndirim mantığı
        if total >= 200.0:
            odenen_tutar = total * 0.85
            print("🎉 200 TL ve üzeri alışverişe %15 İndirim Uygulandı!")
            print(f"İndirimli Toplam: {odenen_tutar:.2f} TL")
            self.fisi_yazdir(sepet_objesi, total, odenen_tutar)
            self.kasa_guncelle(sepet_objesi, odenen_tutar)
        elif total >= 100.0:
            odenen_tutar = total * 0.90
            print("🎉 100 TL ve üzeri alışverişe %10 İndirim Uygulandı!")
            print(f"İndirimli Toplam: {odenen_tutar:.2f} TL")
            self.fisi_yazdir(sepet_objesi, total, odenen_tutar)
            self.kasa_guncelle(sepet_objesi, odenen_tutar)
        else:
            odenen_tutar = total
            print(f"Ödenecek Toplam: {odenen_tutar:.2f} TL (İndirim için en az 100 TL alışveriş yapmalısınız.)")
            self.fisi_yazdir(sepet_objesi, total)
            self.kasa_guncelle(sepet_objesi, odenen_tutar)
    def raporu_yazdir(self):
        self.raporlayici.gun_sonu_raporla()
def main():
    kantin = KantinYonetimi()

    while True:
        print("\n--- İŞLEMLER ---")
        print("1 - Sipariş Ver")
        print("2 - Gün Sonu Kasa Raporunu Gör")
        print("3 - Çıkış")
        secim = input("Seçiminiz (1/2/3): ").strip()

        if secim == "1":
            musteri_sepeti = Sepet()
            while True:
                kantin.menuyu_goster()
                item = (
                    input(
                        "Sipariş etmek istediğiniz ürünü girin (Bitirmek için 'q'): "
                    )
                    .strip()
                    .capitalize()
                )

                if item.lower() == "q":
                    break

                if item not in kantin.menu:
                    print("❌ Geçersiz ürün. Lütfen menüden seçin.")
                    continue

                try:
                    quantity = int(input(f"{item} için adet sayısı: "))
                    if quantity <= 0:
                        print("⚠️ Adet pozitif olmalıdır.")
                        continue
                except ValueError:
                    print("❌ Hatalı giriş! Sayı giriniz.")
                    continue

                musteri_sepeti.urun_ekle(item, quantity)
                print(f"✅ {quantity} adet {item} sepete eklendi.")

            sepet_icerigi = musteri_sepeti.sepeti_goster()
            if sepet_icerigi:
                kantin.hesabi_kes(sepet_icerigi)
            else:
                print("Sepetiniz boş, iyi günler dileriz.")

        elif secim == "2":
            kantin.raporu_yazdir()

            kapanis_sorusu = input("\n🔒 Kasa kapatılsın ve sistemden çıkılsın mı? (E/H): ").strip().lower()
            if kapanis_sorusu == 'e':
                print("👋 Gün sonu tamamlandı, kasa kapatıldı. İyi akşamlar!")
                break
            else:
                print("🔄 Ana menüye dönülüyor...")
                continue

        elif secim == "3":
            print("Çıkış yapılıyor. İyi günler dileriz!")
            break
        else:
            print("❌ Geçersiz seçim! Lütfen 1, 2 veya 3 giriniz.")


if __name__ == "__main__":
    main()