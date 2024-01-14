gorevler = []
while True:
    secim = input("\n Yapmak istediğiniz işlemi seçiniz: 1.Ekle , 2.Sil , 3.Listele \n")

    if secim == "1":
        yeni_gorev = input("görev ekleyin: ")
        gorevler.append(yeni_gorev)
        print("görev eklendi")

    elif secim == "2":
        if gorevler:
            silinecek_gorev = input("Silmek İstdiğiniz Görevi Giriniz:")
            if silinecek_gorev in gorevler:
                gorevler.remove(silinecek_gorev)
                print(f'"{silinecek_gorev}"Görev Silindi')
            else:
                print(f'"{silinecek_gorev}"Görev Bulunamadı')

        else:
            print("Liste boş")

    elif secim == "3": 
        if gorevler:
            print("\n Yapılacaklar Listesi:")
            for index, gorev in enumerate(gorevler, start=1):
                print(f'{index}. {gorev}')
        else:
            print("Yapılacaklar listesi boş.")
        



