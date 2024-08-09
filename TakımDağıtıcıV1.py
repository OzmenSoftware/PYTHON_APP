import random

def ortalama_kademe(takim, kademe_dict):
    toplam_kademe = sum(kademe_dict[isim] for isim in takim)
    return toplam_kademe / len(takim)

def toplam_kademe(takim, kademe_dict):
    return sum(kademe_dict[isim] for isim in takim)

def takim_uygunluk(takim1, takim2, kademe_dict):
    ortalama1 = ortalama_kademe(takim1, kademe_dict)
    ortalama2 = ortalama_kademe(takim2, kademe_dict)
    return abs(ortalama1 - ortalama2)

def rastgele_takimlara_dagit(isimler, kademe_dict):
    while True:
        random.shuffle(isimler)
        
        # İki takıma böl
        takim1 = isimler[:len(isimler)//2]
        takim2 = isimler[len(isimler)//2:]
        
        # Emin ve Mertcan'ın aynı takıma düşmediğinden emin ol
        if "Emin" in takim1 and "Mertcan" in takim1:
            continue
        if "Emin" in takim2 and "Mertcan" in takim2:
            continue

        if "Gökhay" in takim1 and "Hasan" in takim1:
            continue
        if "Gökhay" in takim2 and "Hasan" in takim2:
            continue
        
        
        # Kademe ortalamalarını ve toplamlarını kontrol et
        if takim_uygunluk(takim1, takim2, kademe_dict) <= 1:  # Ortalama farkının 1'den fazla olmaması için kontrol
            return takim1, takim2

# Örnek isim listesi ve kademeler
isimler = ["Özmen", "Emin", "Mertcan", "Nedim", "Hasan", "Emre", "Gökhay", "Ferit", "Sinan", "Enes"]
kademe_dict = {
    "Özmen": 2,
    "Emin": 1,
    "Mertcan": 1,
    "Nedim": 3,
    "Hasan": 3,
    "Emre": 5,
    "Gökhay": 3,
    "Ferit": 5,
    "Sinan": 3,
    "Enes": 2
}

# Takımları oluştur
takim1, takim2 = rastgele_takimlara_dagit(isimler, kademe_dict)

print("Takım 1:", takim1, "Ortalama Kademe:", ortalama_kademe(takim1, kademe_dict))
print("Takım 2:", takim2, "Ortalama Kademe:", ortalama_kademe(takim2, kademe_dict))
