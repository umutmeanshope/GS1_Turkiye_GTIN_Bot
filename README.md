
### English

> Read further for Turkish

# GS1 Türkiye EAN Barcode Registration Bot
This Python script automates the process of registering EAN (European Article Numbers) barcodes on the GS1 Turkey website using the selenium library. The script reads product information from a JSON file, fills out the registration form on the website, and retrieves the generated EAN numbers for each product.

## Features
* Automates the EAN barcode registration process on the GS1 Turkey website.
* Reads product information (brand, name, category, etc.) from a JSON file.
* Automatically inputs data into the appropriate fields on the form.
* Retrieves and saves the generated EAN numbers back into the JSON file.

## Prerequisites

* Python 3.x
* Google Chrome browser installed
* ChromeDriver for Selenium

### Required Python libraries:
* Selenium

You can install the necessary Python packages within the terminal using:

```pip install selenium```

## Setup

1. Download and install ChromeDriver and make sure it's added to your system's PATH.

2. Clone or download this repository and navigate to the project folder.

3. Add your product details to the items.json file in the following format:

```
[
    {
        "Brand": "ExampleBrand",
        "Item Name": "ExampleProduct",
        "Segment": "123",
        "Family": "456",
        "Class": "789",
        "Brick": "1011"
    }
]
```

> **Note:** You can find the Segment, Family, Class and Brick ids you need in the gs1 Türkiye website using inspect feature  

5. Solve the captcha and log in to the GS1 Turkey website. Navigate to the barcode form and press Enter to start the automation process.


## How It Works

1. The script logs in to the GS1 Turkey website using Selenium and waits for manual captcha solving.
2. It retrieves product information from the items.json file.
3. It automates the process of filling out the required forms for each product and submitting them to generate an EAN.
4. The generated EAN is added to the corresponding product data in the items.json file.
5. After processing all items, the script saves the updated items.json file with the new EAN numbers.
### Notes
* The script pauses and waits for the user to solve the captcha before starting the automation.
* Ensure your ChromeDriver version matches your installed Chrome browser version.
* Modify the items.json file as needed to include your product details.
* The script clicks the confirm button after creating a barcode and saves the EAN number to the items.json file.
* This Script is highly specialised to my needs. Your use may vary. You may consider
this script as a demonstration rather than a tool.

## License

Licensed under GPL v3

See: http://www.gnu.org/licenses/.

### Turkish

# GS1 Türkiye EAN Barkod Kayıt Otomasyonu
Bu script, GS1 Türkiye web sitesinde EAN (European Article Numbers) barkodlarının 
kaydedilmesini selenium kütüphanesi kullanarak otomatikleştirir. Ürün bilgilerini 
bir JSON dosyasından okur, web sitesindeki kayıt formunu doldurur ve her ürün için 
üretilen EAN numaralarını json dosyasına kaydeder.

## Özellikler
* GS1 Türkiye web sitesinde EAN barkod kayıt sürecini otomatize eder.
* Ürün bilgilerini (marka, isim, kategori vb.) bir JSON dosyasından okur.
* Verileri ilgili form alanlarına otomatik olarak girer.
* Üretilen EAN numaralarını alır ve JSON dosyasına kaydeder.

## Gereksinimler

* Python 3.x
* Google Chrome tarayıcı
* ChromeDriver for Selenium

### Gerekli Python kütüphaneleri:
* Selenium

Gerekli Python paketlerini yüklemek için:

```pip install selenium```

## Kurulum

1. ChromeDriver'ı indirin ve sistem PATH'inize eklediğinizden emin olun.

2. Bu projeyi klonlayın veya indirin ve proje klasörüne gidin.

3. Ürün bilgilerinizi "items.json" dosyasına şu formatta ekleyin:

```
[
    {
        "Brand": "ExampleBrand",
        "Item Name": "ExampleProduct",
        "Segment": "123",
        "Family": "456",
        "Class": "789",
        "Brick": "1011"
    }
]
```

> **Note:** Segment, Family, Class and Brick numaralarına gs1 
> Türkiye websitesinde Chrome tarayıcısının inspect özelliğini kullanarak ulaşabilirsiniz.
5. Captcha'yı çözün ve GS1 Türkiye web sitesine giriş yapın. 
Barkod formuna gidin ve otomasyon sürecini başlatmak için Enter tuşuna basın.

## Nasıl Çalışır

1. Script Selenium kullanarak GS1 Türkiye web sitesine giriş yapar ve 
captcha'nın manuel olarak çözülmesini bekler.
2. items.json dosyasından ürün bilgilerini alır.
3. Her ürün için gerekli formları doldurma ve göndermeyi otomatikleştirir.
4. Oluşturulan EAN, ilgili ürün bilgilerine eklenir ve items.json dosyasına
kaydedilir.
5. Tüm ürünler işlendiğinde, betik yeni EAN numaraları ile güncellenmiş
items.json dosyasını kaydeder.
### Notlar
* Betik, captcha'nın çözülmesi için kullanıcıdan bekler ve ardından
otomasyona başlar.
* ChromeDriver sürümünüzün, kurulu olan Chrome tarayıcı sürümünüzle 
uyumlu olduğundan emin olun.
* Ürün bilgilerinizi eklemek veya düzenlemek için items.json dosyasını düzenleyin.
* Barkod oluşturulduktan sonra onay butonuna tıklar ve EAN numarasını 
items.json dosyasına kaydeder.
* Bu script çoğunlukla benim ihtiyaçlarıma göre özelleştirilmiştir. 
İhtiyaçlarınıza göre deneyiminiz değişebilir. Bu script bir araçtan çok bir deney ve sunum olarak değerlendirilebilir.

## Lisans

GPL v3 altında lisanslıdır.

Bakınız: http://www.gnu.org/licenses/.

