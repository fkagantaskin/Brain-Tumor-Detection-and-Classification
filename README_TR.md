# Beyin Tümörü Sınıflandırma (MRI Görüntüleri ile)

Bu proje, beyin tümörlerini "MRI görüntüleri" üzerinden sınıflandırmak amacıyla geliştirilmiştir. Derin öğrenme teknikleri kullanılarak, bir MRI görüntüsünde Tümör olup olmadığı ve varsa üç sınıftan hangisine ait olduğunu belirleyen bir model oluşturulmuştur:  
**Glioma**, **Meningioma**, **Pituitary** ve **No Tumor** (Tümör Yok).

## Kullanılan Veri Seti
- Kaynak: [Kaggle Brain Tumor MRI Dataset]
- Sınıflar:  
   - Glioma  
   - Meningioma  
   - Pituitary  
   - No Tumor

Veri seti eğitim,test ve validation olarak ayrılmıştır. (Validation klasörü kod ile random şekilde oluşturulmuştur.)

## Kullanılan Yöntemler ve Teknolojiler
   - Python
   - TensorFlow / Keras
   - MobileNetV2 (Transfer Learning)
   - Veri Artırma (Data Augmentation)
   - Flask (Web Arayüzü için)
   - NumPy, Matplotlib, Sklearn

## Model Eğitimi
Model, başlangıçta sade haliyle (baseline) eğitilmiş, ardından aşağıdaki geliştirmeler uygulanarak doğruluk oranı artırılmış model(improved) oluşturulmuştur:
   - Önceden eğitilmiş MobileNetV2 modeli kullanılarak transfer learning yapılmıştır.
   - Görüntülerin dönüş, yakınlaştırma, kaydırma gibi işlemlerle çeşitlendirilmesi sağlanmıştır.
   - Doğrulama (validation) seti ile erken durdurma (early stopping) uygulanmıştır.

   > Model Başarı Oranları:
      -Improved Model: ~%98,7
(Detaylı eğitim grafikleri ve classification report teslim edilen dosyalar arasındadır.)

## Web Arayüzü (Flask Uygulaması)
Proje kapsamında geliştirilen web uygulaması sayesinde kullanıcılar, kendi MRI görüntülerini yükleyerek anında tahmin alabilmektedir.

### Kullanım:
1. `app.py` dosyasını çalıştırın:
   ```bash
   python app.py
2. Tarayıcıda http://127.0.0.1:5000/ adresini açın.
3. MRI görüntüsünü yükleyin ve "Tahmin Et" butonuna tıklayın.
4. Modelin tahmini ekranda gösterilecektir.

### Not:
 
* uploads/ klasörü çalışma sırasında otomatik oluşturulur, içerisine web tarayıcı üzerinden tahmin işlemi yapılan görseller otomatik kaydolur. 
