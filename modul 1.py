#tugas 1
class Hero:
    pass
 
hero_1 = Hero()
hero_2 = Hero()
 
hero_1.name = "Goku"
hero_2.name = "Vegeta"
 
hero_1.power = 100
hero_2.power = 90
 

print(hero_1.name)
print(hero_2.name)  
print(hero_1.__dict__)



#tugas 2
class Mahasiswa:
    def __init__(self, name, nim, prodi):
        self.name = name
        self.nim = nim
        self.prodi = prodi
 

mhs1 = Mahasiswa("Firdaus", "21051214005", "Informatika")
mhs2 = Mahasiswa("Budi", "21051214006", "Sistem Informasi")
 

print("Nama:", mhs1.name)
print("NIM:", mhs1.nim)
print("Prodi:", mhs1.prodi)
print(mhs1.__dict__)
print()
print("Nama:", mhs2.name)
print("NIM:", mhs2.nim)
print("Prodi:", mhs2.prodi)
print(mhs2.__dict__)
 
 

#tugas 3
class Mahasiswa:
   
    jumlah_mahasiswa = 0
   
    def __init__(self, name, nim, prodi):
        self.name = name
        self.nim = nim
        self.prodi = prodi
        Mahasiswa.jumlah_mahasiswa += 1
        print("Membuat Object Mahasiswa dengan nama " + self.name)
       
mhs1 = Mahasiswa("Firdaus", "21051214005", "Teknik Informatika")
print("Total Mahasiswa : " + str(mhs1.jumlah_mahasiswa))
mhs2 = Mahasiswa("Budi", "21051214006", "Teknik Industri")
print("Total Mahasiswa : " + str(mhs2.jumlah_mahasiswa))
 
print()
print("Total Mahasiswa : " + str(Mahasiswa.jumlah_mahasiswa))
 
 
 