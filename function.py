def reverse_per_kata(kalimat):
    kata = kalimat.split()      #memisahkan kalimat menjadi list kata
    hasil = []                  #variabel kosong untuk menampung list
    for i in kata:              #looping kata pada variabel kata
        hasil.append(i[::-1])   #membalikan kata dan menambahkan ke variabel hasil
    return ' '.join(hasil)      #menggabungkan kata-kata pada variabel hasil dengan menambahkan spasi

print(reverse_per_kata("AKU CINTA KAMU"))
# Output: "UKA ATNIC UMAK"

def urutkan_kalimat(kalimat, urutan):
    kata = kalimat.split()            #memisahkan kalimat menjadi list kata
    terurut = []                      #variabel kosong untuk menampung list
    for i in urutan:                  #looping inputan list pada parameter urutan
        terurut.append(kata[i - 1])   #menambahkan kata dengan indeks - 1 ke variabel terurut 
    return ' '.join(terurut)          #menggabungkan kata-kata pada variabel hasil dengan menambahkan spasi

print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))
# Output: "PYTHON HARI BELAJAR SEDANG INI"

def ganti_vokal(kalimat, opsi):
    vokal_kecil = {'a' : '4', 'i' : '1', 'u' : '|_|', 'e' : '3', 'o' : '0'}  #kamus vokal kecil
    vokal_besar = {'A' : '4', 'I' : '1', 'U' : '|_|', 'E' : '3', 'O' : '0'}  #kamus vokal besar
    
    hasil = ""                                     #variabel kosong untuk menampung hasil akhir
    for huruf in kalimat:                          #looping inputan pada parameter kalimat
        if opsi == 1 and huruf in vokal_kecil:     #jika opsi 1 dan huruf ada pada vokal kecil
            hasil += vokal_kecil[huruf]            #ganti dengan simbol dari kamus vokal_kecil
        elif opsi == 2 and huruf in vokal_besar:   #jika opsi 1 dan huruf ada pada vokal besar
            hasil += vokal_besar[huruf]            #ganti dengan simbol dari kamus vokal_besar
        else:
            hasil += huruf                         #jika bukan vokal yang ditentukan, biarkan huruf tetap
    return hasil

print(ganti_vokal("Aku Cinta Kamu", 1))
# Output: "Ak|_| C1nt4 K4m|_|"
print(ganti_vokal("Aku Cinta Kamu", 2))
# Output: "4ku Cinta Kamu"