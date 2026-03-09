#!/usr/bin/env python3
import socket
import time
import threading

lock = threading.Lock()

def cokluTara():
    hedef = input("\n\nHedef adres giriniz: ")
    baslangicPort= int(input("Baslangic portunu girin: "))
    bitisPort = int(input("Taranacak son portu giriniz: "))
    sureBaslangic = time.time()
    acikportlar = []
    
    for portt in range(baslangicPort,bitisPort + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((hedef,portt))
            acikportlar.append(portt)
        except (TimeoutError, ConnectionAbortedError, ConnectionRefusedError, socket.gaierror):
            pass
        finally:    
            s.close()
    sureBitis = time.time()
    gecenSure= round(sureBitis - sureBaslangic)
    print(f"Acik portlar: {acikportlar}")
    print(f"Islem {gecenSure} saniyede bitti!")


def tekliTara():
    #Hedef bilgilerini alalim
    hedef = input("\n\nHedef adres giriniz: ")
    portNum = int(input("Hedef port giriniz: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    try:
        s.connect((hedef,portNum))
        print("Hedef port acik!")
    except TimeoutError:
        print("Yanit donmedi, TIMEOUT!")
    except InterruptedError:
        print("Islem iptal ediliyor ...")
    except socket.gaierror:
        print("Adres bulunamadi!")
    except ConnectionRefusedError:
        print("Baglanti reddedildi, port kapali!")
    finally:
        s.close()

def menu():
    print("Port scanner'a hos geldiniz, islem secin\n1-Tek port tarama\n2-Coklu port tarama")
    secim = int(input())
    if secim == 1:
        tekliTara()
    elif secim==2:
        cokluTara()

if __name__ == "__main__":
    menu()