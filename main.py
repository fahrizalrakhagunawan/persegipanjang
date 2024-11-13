# main.py

# fungsi untuk memeriksa apakah input adalah bilangan positif
def input_positif(prompt):
    while true:
        try:
            nilai - float(input(prompt))
            if nilai > 0:
                return nilai
            else:
                print("nilai harus lebih dari 0. coba lagi.")
     except valueerror:
        print("input tidak valid. masukkan angka.")

# meminta input panjang dan lebar dari pengguna dengan validasi
panjang = input_positif("masukkan panjang persegi panjang")
lebar = input_positif("masukkan lebar persegi panjang:")

# menghitung luas 
luas = panjang * lebar
# menghitung keliling 
keliling = 2 *(panjang +lebar)

# menampilkan hasil luas dan keliling dengan format yang lebih jelas
print(f"luas persegi panjang adalah {luas} satuan persegi")
print(f"keliling persegi panjang adalah {keliling} satuan")


