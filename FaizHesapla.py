import math

def bilesik_faiz(anapara, faiz_orani, bileşik_sayisi, zaman):
    toplam_miktar = anapara * math.pow((1 + faiz_orani / bileşik_sayisi), (bileşik_sayisi * zaman))
    return toplam_miktar

def anuite_hesapla(anapara, aylik_faiz_orani, toplam_ay):
    aylik_odeme = (anapara * aylik_faiz_orani * math.pow(1 + aylik_faiz_orani, toplam_ay)) / (math.pow(1 + aylik_faiz_orani, toplam_ay) - 1)
    return aylik_odeme

def main():
    # Kullanıcıdan verileri al
    anapara = float(input("Anapara miktarını girin: "))
    faiz_orani = float(input("Yıllık faiz oranını girin (yüzde olarak, örneğin 5 için 0.05 girin): "))
    bileşik_sayisi = 12  # Aylık bileşik faiz
    
    # Vadeler
    vadeler = [6, 12, 24, 36]
    
    # Her vade için bileşik faiz hesapla
    for vade in vadeler:
        toplam_miktar = bilesik_faiz(anapara, faiz_orani, bileşik_sayisi, vade / 12)  # vade ay cinsinden olduğu için yıl cinsine çeviriyoruz
        aylik_faiz_orani = faiz_orani / 12
        aylik_odeme = anuite_hesapla(toplam_miktar, aylik_faiz_orani, vade)
        print(f"{vade} ay sonunda toplam miktar: {toplam_miktar:.2f} TL, aylık ödeme: {aylik_odeme:.2f} TL")
    
if __name__ == "__main__":
    main()
