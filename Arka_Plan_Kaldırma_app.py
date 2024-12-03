from tkinter import *
from tkinter import filedialog , messagebox
from rembg import remove 
from PIL import Image,ImageTk
import io

#Arka planı kaldırma

def arka_plan_kaldir():
    try:
        #kullanıcıdan dosya sec
        girdi_dosya = filedialog.askopenfilename(
            title="Bir Görüntü Seçin",
            filetypes=[("Image Files","*.jpg *.jpeg *.png")] #kabul edilen dosya tipleri
        )
        #eger kullanıcı bir dosya secmezse başa sar
        if not girdi_dosya:
            return
        
        cikti_dosya = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files","*.png")],
            title="Çıktı Dosyasını Kayıt Et"
        )
        if not cikti_dosya:
            return
      
        # Görüntüyü oku ve arkaplanı kaldır
        with open(girdi_dosya,"rb") as dosya: #dosya okuma modunda acılıcak
            girdi = dosya.read() 
        sonuc = remove(girdi) #arka planı kaldırıyoruz

        #cıktı dosyasını yazarız
        with open(cikti_dosya,"wb") as dosya:
            dosya.write(sonuc) #islenmis goruntuyu yenı dosyaya yazar


        #cıktı goruntusune bir onızleme ekle
        sonuc_goruntu = Image.open(io.BytesIO(sonuc))
        sonuc_goruntu.thumbnail((300,300))
        sonuc_img = ImageTk.PhotoImage(sonuc_goruntu)
        label_cikti.config(image=sonuc_img)
        label_cikti.image=sonuc_img 


    except Exception as e:
        messagebox.showerror("Hata",f"Bir hata olutşu: {e}")


#arayüzü
pencere = Tk()
pencere.title("Arka Plan Kaldırma Uygulaması - Furkan Ekinci")
pencere.geometry("500x400")

#baslık etiketleri
label_baslik= Label(pencere,text="Fotoğraflardaki Arka Planı Kaldır",font=("Arial",16))
label_baslik.pack(pady=10)

buton_islem = Button(pencere, text="Görsel seç ve arka plan kaldır",command=arka_plan_kaldir)
buton_islem.pack(pady=20)

#çıktı görüntüsü için label
label_cikti=Label(pencere)
label_cikti.pack(pady=10)


pencere.mainloop()