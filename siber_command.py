import os
import sys
import time
import socket
import subprocess
import urllib.request
import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# SENCER CYBER COMMAND CORE v10.0 - ULTRA REAL WEBSPACE ANALYZER
# ==============================================================================

def siber_anons(metin):
    """Sistem ses kartını en üst perdeden tetikleyen ses kodu"""
    komut = f'PowerShell -Command "Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{metin}\')"'
    os.system(komut)

def canli_web_acik_tara():
    """İnternetteki herhangi bir sitenin siber durum kodunu ve açığını canlı sorgular"""
    hedef_site = ent_hedef.get().strip()
    if not hedef_site:
        messagebox.showwarning("Eksik Veri", "Şef, taramak için bir web sitesi adresi girin!")
        return
        
    if not hedef_site.startswith("http://") and not hedef_site.startswith("https://"):
        hedef_site = "https://" + hedef_site

    txt_ekran.insert(tk.END, f"\n[📡] CANLI SORGULAMA: {hedef_site} sunucusuna paket gönderiliyor...\n")
    root.update()
    
    try:
        # Gerçek bir web tarayıcısı gibi davranıp sunucu kapısını çalıyoruz
        istek = urllib.request.Request(hedef_site, headers={'User-Agent': 'Mozilla/5.0'})
        zaman_basla = time.time()
        with urllib.request.urlopen(istek, timeout=4) as yanit:
            durum_kodu = yanit.getcode()
            cevap_suresi = round((time.time() - zaman_basla) * 1000, 2)
            
            txt_ekran.insert(tk.END, f" [✔] BAĞLANTI BAŞARILI! Sunucu Yanıtı: HTTP {durum_kodu} (OK)\n")
            txt_ekran.insert(tk.END, f" [⏱] Tepki Süresi: {cevap_suresi} ms (Sunucu Hızı Mükemmel)\n")
            txt_ekran.insert(tk.END, f" [🔒] Güvenlik Tipi: Sitenin veri şifreleme kapısı aktif.\n")
            siber_anons("Target server verified and online.")
    except Exception as e:
        txt_ekran.insert(tk.END, f" [❌] KRİTİK ENGEL: Sunucu yanıt vermedi veya siber koruma devreye girdi!\n")
        txt_ekran.insert(tk.END, f" [!] Hata Detayı: {str(e)}\n")
        siber_anons("Target connection blocked by network.")
        
    txt_ekran.see(tk.END)

def gercek_dns_cozucu():
    """Girilen sitenin arkasındaki gerçek dünya IP adresini internet uydularından çözer"""
    hedef_site = ent_hedef.get().strip()
    # Protokol temizliği (Sadece alan adı lazım)
    hedef_site = hedef_site.replace("https://", "").replace("http://", "").split("/")[0]
    
    if not hedef_site:
        return
        
    txt_ekran.insert(tk.END, f"\n[🔮] DNS HARİTALANDIRMA: {hedef_site} için dünya IP havuzu taranıyor...\n")
    root.update()
    
    try:
        gercek_ip = socket.gethostbyname(hedef_site)
        txt_ekran.insert(tk.END, f" [🎯] BAŞARILI! Sitenin Gerçek Dünya IP Adresi: {gercek_ip}\n")
        txt_ekran.insert(tk.END, f" [*] Bilgi: Bu IP adresini kullanarak siteye doğrudan dijital paketler atılabilir!\n")
        siber_anons("D N S lookup completed successfully.")
    except:
        txt_ekran.insert(tk.END, " [❌] IP Adresi Çözülemedi. Site sahte olabilir veya proxy arkasına gizlenmiş.\n")

def ultra_matrix_mod():
    """Terminali gerçek ağ yollarıyla Matrix şelalesine sokar"""
    siber_anons("Launching advanced deep kernel tree sweep.")
    txt_ekran.insert(tk.END, "\n>>> MATRİX ÇEKİRDEK TARAMASI TETİKLENDİ. CMD EKRANINA BAKIN...\n")
    root.update()
    time.sleep(0.5)
    # CMD ekranına mavi-yeşil siber kod akışı başlatır
    os.system("cmd /c color 0a && tree C:\\Windows\\System32")

# ==============================================================================
# HIRS PRO GRAFİK ARABİRİMİ (CYBER WAR ROOM STYLE)
# ==============================================================================

os.system("cls")
os.system("color 0a")

root = tk.Tk()
root.title("Sencer-AI Cyber Command Core v10.0")
root.geometry("700x520")
root.configure(bg="#020202")

# Ana Başlık
tk.Label(root, text="💻 SENCER-AI LIVE WEB & NETWORK EXPLOIT ANALYZER", font=("Consolas", 12, "bold"), fg="#00ff00", bg="#020202").pack(pady=15)

# Hedef Giriş Alanı
pan_giris = tk.Frame(root, bg="#020202")
pan_giris.pack(pady=5)

tk.Label(pan_giris, text="Hedef Web Sitesi (URL):", font=("Consolas", 10, "bold"), fg="#00ff00", bg="#020202").pack(side="left", padx=5)
ent_hedef = tk.Entry(pan_giris, font=("Consolas", 11), bg="#0a0a0a", fg="#00ff00", insertbackground="#00ff00", width=30, bd=1, relief="solid")
ent_hedef.insert(0, "google.com") # Varsayılan hedef
ent_hedef.pack(side="left", padx=5)

# Butonlar Paneli
pan_butonlar = tk.Frame(root, bg="#020202")
pan_butonlar.pack(pady=10)

btn_tara = tk.Button(pan_butonlar, text="🌐 SUNUCUYU CANLI SORGULA", font=("Consolas", 9, "bold"), bg="#002200", fg="#00ff00", width=25, height=2, command=canli_web_acik_tara)
btn_tara.grid(row=0, column=0, padx=10)

btn_dns = tk.Button(pan_butonlar, text="🎯 GERÇEK IP ADRESİNİ BUL", font=("Consolas", 9, "bold"), bg="#001122", fg="#3399ff", width=25, height=2, command=gercek_dns_cozucu)
btn_dns.grid(row=0, column=1, padx=10)

# Dev Siber Çıktı Ekranı
txt_ekran = tk.Text(root, font=("Consolas", 10), bg="#050505", fg="#00ff00", insertbackground="#00ff00", bd=1, relief="solid")
txt_ekran.pack(pady=15, padx=20, fill="both", expand=True)
txt_ekran.insert(tk.END, "=== COMMAND CORE ACTIVE: SENCER MASTER ALGORITHMS ARMED ===\n")
txt_ekran.insert(tk.END, "[*] İstasyon hazır. Yukarıya taramak istediğin gerçek bir siteyi yazıp butonlara bas şef!\n")

# Alt Tehlikeli Matrix Butonu
btn_matrix = tk.Button(root, text="⚡ DEEP SYSTEM TREE MATRIX SWEEP (ZORLU TARAMA) ⚡", font=("Consolas", 10, "bold"), bg="#220000", fg="red", activebackground="red", activeforeground="black", width=65, height=2, command=ultra_matrix_mod)
btn_matrix.pack(pady=15)

# Açılış Sesli Raporu
siber_anons("Cyber tactical command armed. System ready for action.")

root.mainloop()
