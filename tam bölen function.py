

def tam_bolen(sayı):
    liste = []

    for i in range(2,sayı+1):
        if sayı % i == 0:
            liste.append(i)
    return liste


while True:
    sayı = input("Sayı:")

    if sayı == "q":
        print("Programdan Çıkılıyor..")
        break

    else:
        sayı = int(sayı)
        print("Tam Bölenler",tam_bolen(sayı))


