contohList = ["ayam", 1, 2, True, True] 
lagiList = [10, 20, 1, 30, 2, 3, 5, 32, 12]


contohVar = "bebek"




for x in range(10):
    #print(x, end= "")
    for y in range(10):
        print(y, end= "")
        if x == y:
            break
    print("")


print("")
print("")



for x in range(10):
    # print(x, end="")
    for y in range(10):
        print(y, end="")
        if x+y == 9: 
            break
    print("")    
    
print("")
print("")
    
for x in range(10): 
    print(x, end="")
    for y in range(20):
        print(y, end="")
    print("")
    
    
    
print("")
print("")

lagiList.sort()

for x in range(5):
    print("x")
    for y in lagiList: 
        print(y, end="")



print("")
print("")

# soal 1 
list1 = [1,2,3,4,5]
list2 = [9,8,7,6,5] # soalnya adalah gimana caranya menampilkan 10 dengan cara menjumlahkan kedua list

for i in range(len(list1)):
    print(list1[i] + list2[i])
        
    
print("")
print("")


# soal 2
var1 = "namaku"
var2 = ["falah", "nasya", "cantik", "ganteng"] # soalnya adalah gimana caranya menampilkan namaku falah dst dr kedua list 

print(var1)
print(var2)

for i in range(len(var2)):
    print(var1, var2[i])
    

print("")
print("")

var1 = "namaku"
var2 = ["falah", "nasya", "cantik", "ganteng"]

print(var1)
print(var2)

for i in range(len(var2)):
    print(var1, var2[i])


print("")
print("")

list1 = [10, 20, 30, 40, 50]
list2 = [1, 2, 3, 4, 5]

# jawabannya adalah listbaru = [9, 18, 27, 36, 45]

listBaru = []

for x in range(len(list1)):
    nilai = list1[x] * list2[x]
    listBaru.append(nilai)
   
print(listBaru)

for i in listBaru:
    if i > 50: 
        print(i)


print("")
print("")

var = "PYTHON"

# P
# PY
# PYT
# PYTH
# PYTHO
# PYTHON

for i in range(len(var)):
    for y in range(len(var)):
        print(var[y], " ", end="")
        if var[i] == var[y]:
            break
    print("")
    
print("")
print("")    
    
list1 = ["Apel", "Jeruk", "Mangga"]
list2 = ["Merah", "Oranye", "Kuning"]

for x in range(len(list1)):
    print(list1[x], " - ", list2[x])
    
print("")
print("")    

list1 = [3, 6, 9, 12, 15, 5]
list2 = [5, 10, 15, 20, 25, 1]

# mencari elemen yang sama pada dua list dan masukkan ke list baru 

for i in range(len(list1)):
    for y in range(len(list1)):
        if list1[i] == list2[y]:
            print(list1[x])


print("")
print("")

# MENCARI 2 ELEMEN YG SAMA pada sebuah list 

# Data
listPertama = [3, 6, 9, 12, 15, 5]
listKedua = [5, 10, 15, 20, 25, 1]

nilai = len(listPertama)
listBaru = []

for x in range(nilai): 
    for y in range(nilai): 
        if listPertama[x] == listKedua[y]:
            print(listKedua[y])
            print(listPertama[x], " dan ", listKedua[y], "SAMA")
            listBaru.append(listPertama[x])
        else: 
            print(listPertama[x], " dan ", listKedua[y], "Tidak sama")
        
        
    print("")    

print("List yang memiliki nilai sama:", listBaru)


print("")
print("")

print(set(listPertama))
print(set(listKedua))


print("")