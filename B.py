# sekarang waktunya function 
# anjay keren sekali bukan 
# sudah sampai function cuy
# semangat belajar 
# biar jadi software engineer di google 

# Coba sekarang tambahkan list biar lebih paham 

data = ["Ayam", "Bebek", False, "Nigga", 10, 2, 4, True]
dataangka = [10, 3, 2, 5, 12, 43, 23, 1]


# anjay sekarang nyoba rekursi yok 

nilai = 10

def rekursi(param):  
    if param != 0: 
        print(param)
        param-=1
        rekursi(param)
    else: 
        return
        
rekursi(nilai)


print("")
print("")

# input: 5
# output: 5 4 3 2 1 

#userInput = input()
#userInput = int(userInput)

#def soalRekursi(param): 
#    if param != 0: 
#        print(param, end=" ")
#        param-=1
#        soalRekursi(param)
#    else: 
#        return 
    
#soalRekursi(userInput)


print("")
print("")


# faktorial
# input: 5
# output: 120 (karena 5! = 5 * 4 * 3 * 2 * 1 = 120)


def rekursiFaktorial(param):
    if param != 1 : 
        return param * rekursiFaktorial(param-1)
    else:
        return 1
        
print(rekursiFaktorial(5))

# yang ini dijumlahkan
def rekursiJumlah(param):
    if param != 1 : 
        return param + rekursiJumlah(param-1)
    else:
        return 1
        
print(rekursiJumlah(5))

print("")
print("")

# Pencarian elemen dalam list 
# Input: List: [3, 5, 7, 9], Elemen: 7
# Output: 2 (karena elemen 7 ada di indeks ke-2)

data = [3, 5, 7, 9]
elemen = 7
i=0

def rekursiCari(param1, param2): 
    if elemen == param1[param2]:
        print(param2)
    else: 
        rekursiCari(param1, param2+1)
    
rekursiCari(data, i)
    

# pangkat(eksponensial) kayaknya gampang nih  
a = 4
n = 2 

def rekursiPangkat(nilai, pangkat):
    if pangkat>1: 
        return nilai*rekursiPangkat(nilai, pangkat-1)
    else: 
        return nilai

print(rekursiPangkat(a, n))


print("")
print("")


## mencari bilangan prima 
# Input: 7
# Output: True (karena 7 adalah bilangan prima)

input=23

def rekursiPrima(cek):
    if cek % 2 == 0:
        return"bilangan genap"
    else: 
        if cek%5 == 0 or cek%3 == 0:     
            return "bilangan ganjil"
        else: 
            return"bilangan prima"
        

print(rekursiPrima(input))

for i in range(100): 
    print(i, " : ", rekursiPrima(i))


print("")
print("")

a


