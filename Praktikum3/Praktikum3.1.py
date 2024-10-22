import math  # Mengimpor modul math untuk menggunakan nilai pi

# Fungsi lambda untuk menghitung luas lingkaran
luas_lingkaran = lambda r: math.pi * r * r  # Rumus luas = π * r^2

# Jari-jari lingkaran yang ingin dihitung
jari_jari = 7
# Menghitung luas lingkaran dengan jari-jari yang diberikan
area = luas_lingkaran(jari_jari)

# Cetak hasil luas lingkaran dengan format dua angka desimal
print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {area:.2f}")

