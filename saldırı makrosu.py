
#! SALDIRI MAKROS !#
import time
import pyautogui

print("!SALDIRI MAKROSU!\n")

while True:
    try:
        sayi = int(input("Gönderelicek mesaj sayısını giriniz: "))
        mesaj = input("Mesajı giriniz: ")
        break
    except:
        print("Hatalı veri girildi!")
print("program 5 saniye içinde başlayacak")
time.sleep(1)
print("program 4 saniye içinde başlayacak")
time.sleep(1)
print("program 3 saniye içinde başlayacak")
time.sleep(1)
print("program 2 saniye içinde başlayacak")
time.sleep(1)
print("program 1 saniye içinde başlayacak")
time.sleep(1)
print("!Program başladı!")
loop = 0
while loop != sayi:
    pyautogui.write(mesaj)
    pyautogui.press("enter")
    loop = loop+1
print("Saldırı tamamlandı")
time.sleep(100)
print("Sonra görüşürüz!")