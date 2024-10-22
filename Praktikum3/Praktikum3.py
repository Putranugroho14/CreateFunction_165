# Fungsi untuk mengonversi suhu
def konversisuhu(temperature, value):
    if value == 'C':  # Jika suhu dalam Celsius
        # Konversi dari Fahrenheit ke Celsius
        temperaturesuhu = (temperature - 32) * 5/9
        return temperaturesuhu, 'C'  # Kembalikan suhu dan unit 'C'
    else:  # Jika suhu dalam Fahrenheit
        # Konversi dari Celsius ke Fahrenheit
        temperaturesuhu = (temperature * 9/5) + 32
        return temperaturesuhu, 'F'  # Kembalikan suhu dan unit 'F'

# Suhu dalam Celsius yang ingin dikonversi
celsius_temperature = 30
# Konversi Celsius ke Fahrenheit
temperaturesuhu, target_value = konversisuhu(celsius_temperature, 'F')
# Cetak hasil konversi
print(f"{celsius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}")

# Suhu dalam Fahrenheit yang ingin dikonversi
fahrenheit_temperature = 86
# Konversi Fahrenheit ke Celsius
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
# Cetak hasil konversi
print(f"{fahrenheit_temperature}°F dikonversi ke Celsius adalah {temperaturesuhu}°{target_value}")
