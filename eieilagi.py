import random
import time
import pandas 


# Ukuran populasi
UKURAN_POPULASI = 600
# Gen yang valid
GEN = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890'''
# String target yang ingin dihasilkan
TARGET = "Tidak ada yang punya NIM 163221100"

# Membuat gen secara acak dengan panjang tertentu
def buat_gen(length):
    gen = []
    for _ in range(length):
        gen.append(random.choice(GEN))
    return gen



# Menghitung tingkat kesesuaian kromosom dengan target
def hitung_kesalahan(chromosome):
    kesalahan = 0
    fitness = 30
    for gs, gt in zip(chromosome, TARGET):
        if gs != gt:
            kesalahan += 1
            fitness -= 1
    return kesalahan, fitness

# Menghasilkan anak dari dua orang tua (par1 dan par2)
def Seleksi(parent1, parent2):
    anak_kromosom = []
    for gen_parent1, gen_parent2 in zip(parent1, parent2):
        probabilitas = random.random()
        if probabilitas < 0.45:
            anak_kromosom.append(gen_parent1)
        elif probabilitas < 0.90:
            anak_kromosom.append(gen_parent2)
        else:
            anak_kromosom.append(random.choice(GEN))
    return anak_kromosom

generasi = 1
ditemukan = False
populasi = []
data_generasi = []


# Mengacak ulang string GEN
GEN = ''.join(random.sample(GEN, len(GEN)))

for _ in range(UKURAN_POPULASI):
  populasi.append(buat_gen(len(TARGET)))

while not ditemukan:
    populasi = sorted(populasi, key=lambda x: hitung_kesalahan(x)[0])
    if hitung_kesalahan(populasi[0])[0] <= 0:
        ditemukan = True
        break


    generasi_terpilih = populasi[:int(0.1 * UKURAN_POPULASI)]
    for _ in range(int(0.9 * UKURAN_POPULASI)):
        induk1 = random.choice(populasi[:300])
        induk2 = random.choice(populasi[:300])
        anak = Seleksi(induk1, induk2)
        generasi_terpilih.append(anak)



    populasi = generasi_terpilih
    kesalahan_terkecil, fitness_terbaik = hitung_kesalahan(populasi[0])
    individu_terbaik = ''.join(populasi[0])
    print(f"Generasi: {generasi}\thasil: {individu_terbaik}\tkesalahan: {kesalahan_terkecil}\tFitness: {fitness_terbaik}")
    generasi += 1
    data_generasi.append({
        "input ": GEN,
        "Generasi": generasi,
        "Hasil": individu_terbaik,
        "Kesalahan": kesalahan_terkecil,
        "Fitness": fitness_terbaik
    })

kesalahan_terkecil, fitness_terbaik = hitung_kesalahan(populasi[0])
individu_terbaik = ''.join(populasi[0])
print(f"Generasi: {generasi}\thasil: {individu_terbaik}\tkesalahan: {kesalahan_terkecil}\tFitness: {fitness_terbaik}")
data_generasi.append({
  "Generasi": generasi,
  "Hasil": individu_terbaik,
  "Kesalahan": kesalahan_terkecil,
  "Fitness": fitness_terbaik
  })




# Membuat data untuk diconvert ke csv #

df = pandas.DataFrame(data_generasi)
df.to_csv('datahasil_optimasi.csv', index=False)