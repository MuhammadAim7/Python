print(20*"-")
print("kalkulator sederhana")
print(20*"-"+"/n")

bil_1 = float(input("masukan Bilangan 1 :"))
operator = input("masukian operator (x,+,-,/) :")
bil_2 = float(input("masukan Bilangan 2 :"))

if operator == "+" :
     hasil = bil_1 + bil_2
     print(f"hasilnya adalah : {hasil}")
elif operator == "x" :
     hasil = bil_1 * bil_2
     print(f"hasilnya adalah : {hasil}")
elif operator == "-" :
     hasil = bil_1 - bil_2
     print(f"hasilnya adalah : {hasil}")
elif operator == "/" :
     hasil = bil_1 / bil_2 
     print(f"hasilnya adalah : {hasil}")              




