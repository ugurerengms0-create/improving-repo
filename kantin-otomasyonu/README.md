# 🏫 İDÜ Kantin Otomasyonu (OOP Versiyon)

İzmir Demokrasi Üniversitesi (İDÜ) kantin yönetimi için geliştirilmiş, **Nesne Yönelimli Programlama (OOP)** prensipleriyle tasarlanmış profesyonel bir konsol otomasyon sistemidir.

---

## 🚀 Projenin Amacı ve Özellikleri
Bu proje; fonksiyonel programlamadan OOP mimarisine geçiş sürecinde, gerçek dünya süreçlerini (sipariş yönetimi, sepet mantığı, indirim hesaplamaları, kalıcı veri saklama ve gün sonu raporlama) kodlamak amacıyla Management Information Systems (YBS) perspektifiyle geliştirilmiştir.

### ✨ Temel Yetenekler:
* **OOP Mimarisi:** `Urun`, `Sepet`, `KantinYonetimi` ve `Raporlama` olmak üzere modüler sınıf yapısı.
* **Akıllı Sepet ve İndirim:** Ürün ekleme, adet kontrolü ve toplam tutara göre dinamik indirim oranları (%10 ve %15).
* **Kalıcı Veri Saklama (JSON):** Yapılan her satışın `kasa_gecmisi.json` dosyasına güvenle kaydedilmesi.
* **Otomatik Fiş Üretimi:** Her sipariş sonrası `siparis_fisi.txt` çıktısı oluşturulması.
* **Z-Raporu (Gün Sonu Analizi):** Kasadaki toplam ciroyu, sipariş sayısını ve ürün bazlı satış adetlerini raporlayan modül.
* **Güvenli Kapanış:** Gün sonu raporu sonrası yönetici onayıyla kasa kapatma ve sistemden çıkış senaryosu.
* **Savunmacı Programlama (Exception Handling):** Dosya okuma/yazma (`FileNotFoundError`, `OSError`) ve yanlış veri girişlerine (`ValueError`) karşı zırhlanmış hata yakalama mekanizmaları.

---

## 🛠️ Kullanılan Teknolojiler
* **Python 3.x**
* **OOP (Object-Oriented Programming)**
* **JSON & File I/O** (Veri kalıcılığı için)
* **Datetime Modülü** (Zaman damgaları ve fiş/raporlama için)

---

## ⚙️ Kurulum ve Çalıştırma

Projeyi bilgisayarınızda çalıştırmak için şu adımları izleyebilirsiniz:
1. Repoyu klonlayın:
   ```bash
   git clone [https://github.com/kullanici-adin/kantin-otomasyonu.git](https://github.com/kullanici-adin/kantin-otomasyonu.git)
2. Proje klasörüne gidin:
   ```bash
    cd kantin-otomasyonu
3. Programı çalıştırın:
   ```bash
    python kantin_oop.py

📊 Menü ve İşlem Rehberi
1 - Sipariş Ver: Menüden ürün seçimi yapıp sepeti oluşturur, tutarı hesaplar ve fiş keser.

2 - Gün Sonu Kasa Raporunu Gör: Kasadaki toplam ciroyu ve ürünlerin kaçar adet satıldığını raporlar, ardından kasayı kapatma seçeneği sunar.

3 - Çıkış: Sistemi güvenli şekilde sonlandırır.

👨‍💻 Geliştirici
Uğur Eren Yeter

İzmir Demokrasi Üniversitesi - Yönetim Bilgi Sistemleri (YBS)