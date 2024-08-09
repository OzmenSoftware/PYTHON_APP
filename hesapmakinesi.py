def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b != 0:
        return a / b
    else:
        return "Bölme hatası: Sıfıra bölme!"

def main():
    print("Basit Hesap Makinesi")
    
    # Kullanıcıdan sayıları al
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))
    
    # Menü
    print("\nYapılacak işlemi seçin:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    secim = input("Seçiminizi girin (1/2/3/4): ")
    
    if secim == '1':
        print(f"Sonuç: {sayi1} + {sayi2} = {toplama(sayi1, sayi2)}")
    elif secim == '2':
        print(f"Sonuç: {sayi1} - {sayi2} = {cikarma(sayi1, sayi2)}")
    elif secim == '3':
        print(f"Sonuç: {sayi1} * {sayi2} = {carpma(sayi1, sayi2)}")
    elif secim == '4':
        print(f"Sonuç: {sayi1} / {sayi2} = {bolme(sayi1, sayi2)}")
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()
