import tkinter as tk
from tkinter import messagebox
import random

class TakimOlusturucu:
    def __init__(self, root):
        self.root = root
        self.root.title("Takım Oluşturucu")
        self.root.geometry("1280x720")

        # Arka planı koyu gri yap
        self.root.configure(bg='#733635')

        self.isimler = []
        self.kademeler = []

        self.create_widgets()

    def create_widgets(self):
        # Ana çerçeve
        main_frame = tk.Frame(self.root, bg="#e4d00a", bd=10, relief=tk.RAISED)
        main_frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)

        # Başlık
        title_label = tk.Label(main_frame, text="İsim ve Kademe Girin", bg="#e4d00a", font=("Arial", 24, "bold"), fg="#733635")
        title_label.pack(pady=20)

        # Girdi çerçevesi
        entry_frame = tk.Frame(main_frame, bg="#e4d00a")
        entry_frame.pack(pady=10)

        # İsim label ve entry
        isim_label = tk.Label(entry_frame, text="İsim:", font=("Arial", 14), bg="#e4d00a", fg="#733635")
        isim_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.isim_entry = tk.Entry(entry_frame, width=40, font=("Arial", 14))
        self.isim_entry.grid(row=0, column=1, padx=10, pady=10)

        # Kademe label ve entry
        kademe_label = tk.Label(entry_frame, text="Kademe:", font=("Arial", 14), bg="#e4d00a", fg="#733635")
        kademe_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.kademe_entry = tk.Entry(entry_frame, width=40, font=("Arial", 14))
        self.kademe_entry.grid(row=1, column=1, padx=10, pady=10)

        # Ekle butonu
        add_button = tk.Button(main_frame, text="Ekle", command=self.ekle, font=("Arial", 14), bg="#733635", fg="white", width=20)
        add_button.pack(pady=10)

        # Takım oluştur butonu
        create_button = tk.Button(main_frame, text="Takım Oluştur", command=self.olustur, font=("Arial", 14), bg="#733635", fg="white", width=20)
        create_button.pack(pady=10)

        # Sonuç label
        self.result_label = tk.Label(main_frame, text="", bg="#e4d00a", font=("Arial", 16), fg="#733635")
        self.result_label.pack(pady=20)

        # Eklenen veriler listesi
        self.data_listbox = tk.Listbox(main_frame, width=60, height=10, font=("Arial", 14), bg="#e4d00a", fg="#733635", selectmode=tk.SINGLE)
        self.data_listbox.pack(pady=10)

    def ekle(self):
        isim = self.isim_entry.get().strip()
        kademe = self.kademe_entry.get().strip()

        if isim and kademe:
            try:
                kademe = int(kademe)
                if kademe < 1 or kademe > 10:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Hata", "Kademe 1 ile 10 arasında olmalıdır.")
                return

            self.isimler.append(isim)
            self.kademeler.append(kademe)

            # Eklenen veriyi listeye ekle
            self.data_listbox.insert(tk.END, f"İsim: {isim}, Kademe: {kademe}")

            self.isim_entry.delete(0, tk.END)
            self.kademe_entry.delete(0, tk.END)

            messagebox.showinfo("Başarı", f"{isim} isimli kişi eklendi.")
        else:
            messagebox.showerror("Hata", "İsim ve kademe girilmelidir.")

    def ortalama_kademe(self, takim, kademe_dict):
        toplam_kademe = sum(kademe_dict[isim] for isim in takim)
        return toplam_kademe / len(takim)

    def takim_uygunluk(self, takim1, takim2, kademe_dict):
        ortalama1 = self.ortalama_kademe(takim1, kademe_dict)
        ortalama2 = self.ortalama_kademe(takim2, kademe_dict)
        return abs(ortalama1 - ortalama2)

    def rastgele_takimlara_dagit(self, isimler, kademe_dict):
        while True:
            random.shuffle(isimler)

            takim1 = isimler[:len(isimler)//2]
            takim2 = isimler[len(isimler)//2:]

            if "Emin" in takim1 and "Mertcan" in takim1:
                continue
            if "Emin" in takim2 and "Mertcan" in takim2:
                continue
            if "Gökhay" in takim1 and "Hasan" in takim1:
                continue
            if "Gökhay" in takim2 and "Hasan" in takim2:
                continue

            if self.takim_uygunluk(takim1, takim2, kademe_dict) <= 0.5:
                return takim1, takim2

    def olustur(self):
        if len(self.isimler) < 2:
            messagebox.showerror("Hata", "En az iki isim girilmelidir.")
            return

        kademe_dict = dict(zip(self.isimler, self.kademeler))
        takim1, takim2 = self.rastgele_takimlara_dagit(self.isimler[:], kademe_dict)

        ortalama1 = self.ortalama_kademe(takim1, kademe_dict)
        ortalama2 = self.ortalama_kademe(takim2, kademe_dict)

        result = (
            f"T: {', '.join(takim1)} | Ortalama Kademe: {ortalama1:.2f}\n"
            f"CT: {', '.join(takim2)} | Ortalama Kademe: {ortalama2:.2f}"
        )

        self.result_label.config(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    app = TakimOlusturucu(root)
    root.mainloop()
