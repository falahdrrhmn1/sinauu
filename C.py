# jadi sederhana sebenernya. ada hal yang harus diketahui dan tidak diketahui
# sekarang kita lanjut ke belajar class
# bagaimana dengan function? apakah sudah aman?
# insyaallah sudah aman
# coba lakukan praktek sementara 

# insyaallah function sudah aman. sekarang lanjut ke class dan objek aja atau lebih tepatnya oop

# jadi dalam oop terdapat beberapa katergori yang harus dipelajarin. diantaranya sebagai berikut: 
# gausah dibahas. mending langsung praktek aja seperti biasa 

#class mahasiswa(): 
#    nama = "falah"
#    nim = 20 
    
# cara membuat objek 
#contohObjek = mahasiswa.nama

#print(contohObjek)


# nah sudah selesai, itu adalah contoh kelas dan objek yang paling sederhana. akan tetapi ada contoh class dan objek yang lebih penting. yang menerapkan init function 
# jadi setiap class memiliki function yang bernama __init__(). yang mana akan otomatis tereksekusi ketika kelas pertama kali dipanggil

# gunakakan fungsi __init__ untuk memasukkan nilai ke properti objek. sebagai contoh berikut:  

# mencoba menambahkan init pada kelas kita 
class mahasiswa: 
    def __init__(self,nama): 
        self.nama =nama

mahasiswa1 = mahasiswa("falah") 

print(mahasiswa1.nama)
    
    
    
    
    
    
    
# ada istilah baru nih. jadi disini kan function didalam kelas/ konstruktor lebih tepatnya. nah permasalahannya adalah pada parameternya yang ketika mau digunakan harus menggunakan self. akan membingungkan sekali bukan. 
# jadi gini penjelasnnya
