import cv2 as cv
import numpy as np
from operator import itemgetter

#Kapıdan geçildi mi kontrol değeri
ctrl=0


#Hareket fonksiyonları
def Go_Forward():
    return "Go Forward!"

def Go_Backward():
    return "Go Backward!"

def Go_Left():
    return "Go Left!"

def Go_Right():
    return "Go Right!"

def Go_Upward():
    return "Go Upward!"

def Go_Downward():
    return "Go Downward!"

def Pitch_Up():
    return "Pitch Up!"

def Pitch_Down():
    return "Pitch Down!"

def Yaw_Left():
    return "Yaw Left!"

def Yaw_Right():
    return "Yaw Right!"


#Bu fonksiyon video karesini tarar ve etrafına yeşil kareler çizerek sarı çemberleri gösterir. Etrafına kare çizili çemberlerin çıktısını verir.
def Scan_Frame(img):

    yellow_circle = img.copy()
    img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower = np.array([22, 93, 0], dtype="uint8")
    upper = np.array([45, 255, 255], dtype="uint8")
    mask = cv.inRange(img, lower, upper)

    circles = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    circles = circles[0] if len(circles) == 2 else circles[1]

    for c in circles:
        x,y,w,h = cv.boundingRect(c)
        cv.rectangle(yellow_circle, (x, y), (x + w, y + h), (36,255,12), 2)

    cv.imshow('Yellow Circle', yellow_circle)

    cv.waitKey(1)

    return circles


#Bu fonksiyon çemberlerin arrayini alır ve en büyük karenin boyutlarını çıktı olarak verir.
def Select_Big(circles):
    Circles=[]

    for c in circles:
        x,y,w,h=cv.boundingRect(c)
        Circles.append([x,y,w,h,w*h])

    #Çemberleri alanlarına göre küçükten büyüğe sıralma.
    Circles=sorted(Circles,key=itemgetter(4))

    #En büyük çemberin boyutlarını alma.
    x=Circles[-1][0]
    y=Circles[-1][1]
    w=Circles[-1][2]
    h=Circles[-1][3]

    return x,y,w,h


#Bu fonksiyon çembere belli mesafeye kadar yaklaşınca aktifleşir. Taranan çemberin tam olarak ortalanmasını sağlar. Ardından kapıdan geçilmesini sağlar ve kontrol değerini değiştirir.
def Arrange_and_Pass(h_L,w_L):

    while True:
        #Kapıya yukardan aşağı doğru bakılıyorsa aracın yönünü yukarı çevirip aşağı gider ve çemberin ortalanıp ortalanmadığını kontrol eder.
        print(Pitch_Up())
        print(Go_Downward())
        if h_L[1]>h_L[0]:
            #kapıya sağ taraftan bakılıyorsa aracın yönünü sağa çevirip sola gider ve çemberin ortalanıp ortalanmadığını kontrol eder.
            print(Yaw_Right())
            print(Go_Left())
            if w_L[1]>w_L[0]:
                #Eğer çember ortalandıysa kapıdan geçilir.
                print(Go_Forward())
                break
            elif w_L[1]<w_L[0]:
                print(Yaw_Left())
                print(Go_Right())
                print(Go_Forward())
                break

        print(Pitch_Down())
        print(Go_Upward())
        if h_L[1]>h_L[0]:
            print(Yaw_Right())
            print(Go_Left())
            if w_L[1]>w_L[0]:
                print(Go_Forward())
                break
            elif w_L[1]<w_L[0]:
                print(Yaw_Left())
                print(Go_Right())
                print(Go_Forward())
                break

    #Kontrol değeri değiştirilerek kapıdan geçilip geçilmedğinin kontrolü main fonksiyonu içinde kontrol edilir.
    global ctrl
    ctrl=1


#Bu fonksiyon en büyük kare bulunduğunda aktifleşerek aracın gerekli hareketleri yaparak çembere yaklaşmasını sağlar.
def Moving(img,h_L,w_L):

    height = img.shape[0] #Verilen karenin yüksekliği
    width = img.shape[1] #Verilen karenin genişliği


    circles=Scan_Frame(img)
    x,y,w,h=Select_Big(circles)

    #En büyük çemberin merkezlerinin hesaplanıp bir değere atanması
    center_x=int(x+(w/2))
    center_y=int(y+(h/2))

    #Bu fonksiyonda ekran tam ortadan yatay ve tam ortadan dikey iki çizgiyle dörde ayrılarak çemberin konumunun nerede olduğuna göre hareketleri yapmak için yazıldı
    #Ekranı dörde bölmek için gerekli değerler
    O_x=int(width/2) #X ekseninin 0 noktasının pikseli
    O_y=int(height/2) #Y ekseninin 0 noktasının pikseli

    #Hesaplamalarla gerekli hareketler.

    #Eğer çember sağ üstteki dikdörtgende kalıyorsa
    if center_x>O_x and center_y>O_y:
        #Çembere yeterince yaklaşılıp yaklaşılmadığının kontolü
        if h<620:
            print(Yaw_Right())
            print(Pitch_Up())
            print(Go_Forward())
        #Çembere yeterince yaklaşılmış. Bu durumda aracın gerekli eksenlerde düz hale getirilerek kapıdan geçirilmesi
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çember sağ alttaki dikdörtgende
    elif center_x>O_x and center_y<O_y:
        if h<620:
            print(Yaw_Right())
            print(Pitch_Down())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çember sol üstteki dikdörtgende
    elif center_x<O_x and center_y>O_y:
        if h<620:
            print(Yaw_Left())
            print(Pitch_Up())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çember sol alttaki dikdörtgende
    elif center_x<O_x and center_y<O_y:
        if h<620:
            print(Yaw_Right())
            print(Pitch_Down())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çemberin merkezi ortalama olarak pozitif x ekseni üzerinde kalıyorsa
    elif center_x>O_x and (center_y+10==O_y or center_y-10==O_y):
        if h<620:
            print(Yaw_Right())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çemberin merkezi ortalama olarak negatif x ekseni üzerinde kalıyorsa
    elif center_x<O_x and (center_y+10==O_y or center_y-10==O_y):
        if h<620:
            print(Yaw_Left())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çemberin merkezi ortalama olarak pozitif y ekseni üzerinde kalıyorsa
    elif (center_x+10==O_x or center_x-10==O_x) and center_y>O_y:
        if h<620:
            print(Pitch_Up())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çemberin merkezi ortalama olarak negatif y ekseni üzerinde kalıyorsa
    elif (center_x+10==O_x or center_x-10==O_x) and center_y<O_y:
        if h<620:
            print(Pitch_Down())
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

    #Çemberin merkezi ortadaysa
    elif center_x==O_x and center_y==O_y:
        if h<620:
            print(Go_Forward())
        elif h>=620:
            Arrange_and_Pass(h_L, w_L)

#Bu fonksiyon kapıdan geçilip geçilmediğinin kontrolünü yaparak gerekli fonksiyonların aktifleştirilmesini sağlıyor
def main():

    #Arrange and Pass fonksiyonunda kontrollerin yapılabilmesi için her bir video karesinde  bir önceki video karesindeki karenin yüksekliğine ve genişliğine ihtiyaç duyulduğu kıyaslama yapmak için oynayan karedeki ve bir önceki kardeki değerleri tutan listeler
    h_L=[] #2 elemanlı yükseklik listesi
    w_L=[] #2 elemanlı genişlik listesi

    capture = cv.VideoCapture('Data/1.avi')

    #h_L ve w_L listelerini iki elemanlı yapmak için video karesi sayacı
    i = 0
    while True:

        isTrue, frame = capture.read()
        img=frame

        #listelere değerlerin atanması
        h_L.append(Select_Big(Scan_Frame(img))[3])
        w_L.append(Select_Big(Scan_Frame(img))[2])

        #Eğer 2 kare geçtiyse 3. kare oynuyorsa gereksiz olan 1. karenin verisinin silinmesi için gerekli kontroller
        #2 video karesi geçti
        if i>=2:
            #Değerlerin silinmesi
            h_L.pop(0)
            w_L.pop(0)

            #Kapıdan geçip geçilmediğinin kontrolü
            global ctrl
            #Arrange and Pass fonksiyonu çalışmış ve kapıdan geçilmiş
            if ctrl==1:
                print("Gate is passed!!!\n\n")
            #Kapıdan geçilmemiş
            elif ctrl==0:
                #Beş çemberden fazla algılandıysa görüntü kumlu olduğundan daha iyi algılamak için düz git komutu
                if len(Scan_Frame(img)) > 5:
                    print(Go_Forward())
                    print("\n\n")
                #Beş çemberden az algılandı Moving fonksiyonunu aktifleştir ve gerekli hareketleri yap
                elif len(Scan_Frame(img)) <= 5:
                    Moving(img, h_L, w_L)
                    print("\n\n")

        #2 kare geçmemiş
        elif i<2:
            print(len(Scan_Frame(img)))

            if len(Scan_Frame(img)) > 5:
                print(Go_Forward())
                print("\n\n")
            elif len(Scan_Frame(img)) <= 5:
                Moving(img, h_L, w_L)
            print("\n\n")

        i+=1

        if cv.waitKey(1) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

main()

#Bu kodu çalıştırırken şöyle bir hata ile karşılaştım. Videolardaki araçları ben kontrol etmediğim için araçların hareketi ile verilen komutlar uymuyor.
#Şöyle örneklemek gerekirse videodaki araç aşağı gidip düz gider, benim kontrol ettiğim araç ise pitch down yapıp düz giderse sonuç olarak aynı yere varmış oluruz.
#Bu kodda videodlardaki araçların hareketlerinin aynılarını oluşturacak bir algoritmadan çok kendim aracı nasıl hareket ettiririm şeklinde bir algoritma yazdım.

#Sait Metin Yurdakul