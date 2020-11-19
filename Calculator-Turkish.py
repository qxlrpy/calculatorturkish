import colorama
from colorama import Fore, Back, Style
colorama.init()
print(Fore.RED)
print("------------------------------------------------------------------------------------------------------------------------")
print("                    NO MATTER WHAT               †qxlrpy†              EVERYWHERE AT EVERYTIME                          ")
print("------------------------------------------------------------------------------------------------------------------------")
print(Style.RESET_ALL)
print("Python Hesap Makinesi")
isaretler = """
+ , - , * , / , q
"""
while True:
    print(Fore.WHITE + Back.GREEN)
    print(isaretler)

    isaret = input("Islem yapmak istediginiz isareti giriniz)(q=Cikis): ")

    if (isaret == "q"):
        print("Cikis yapiliyor..")
        break

    if (isaret == "+"):
        print("Islem baslatiliyor...")
        print("Eğer sayi yok ise 0 yaziniz")
        sayi1 = input("1. sayiyi giriniz: ")
        sayi2 = input("2.sayiyi giriniz: ")
        sonuc=float(sayi1)+float(sayi2)
        print("Sonuc: " + format(sonuc))
    elif(isaret == "-"):
        print("Islem baslatiliyor...")
        print("Sayilari buyukten kucuge yaziniz")
        sayi1 = input("1. sayiyi giriniz: ")
        sayi2 = input("2.sayiyi giriniz: ")
        sonuc=float(sayi1)-float(sayi2)
        print("Sonuc: " + format(sonuc))
    elif(isaret == "*"):
        print("Islem baslatiliyor...")
        sayi1 = input("1. sayiyi giriniz: ")
        sayi2 = input("2.sayiyi giriniz: ")
        sonuc=float(sayi1)* float(sayi2)
        print("Sonuc: " + format(sonuc))
    elif(isaret == "/"):
        print("Islem baslatiliyor...")
        print("Sayilari buyukten kucuge yaziniz")
        sayi1 = input("1. sayiyi giriniz: ")
        sayi2 = input("2.sayiyi giriniz: ")
        sonuc=float(sayi1) // float(sayi2)
        print("Sonuc: " + format(sonuc))
    print(Style.RESET_ALL)
    print(Fore.RED)
    print("------------------------------------------------------------------------------------------------------------------------")
    print("                    NO MATTER WHAT               †qxlrpy†              EVERYWHERE AT EVERYTIME                          ")
    print("------------------------------------------------------------------------------------------------------------------------")
    print(Style.RESET_ALL)
