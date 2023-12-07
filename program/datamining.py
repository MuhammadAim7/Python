x =int( input("Masukan tahun prediksi :"))
print( 10*"-")
print( "")
print( "")
x1 =x-10
x2 =x1+1
x3 =x2+1
x4 =x3+1
x5 =x4+1
x6 = x5+1
x7 =x6+1
x8 =x7+1

x9 =x8+1
x10 =x9+1
print( 50*"-")

y1 = int(input("masukan jumlah penduduk 10 thn yang lalu "+" :"))
y2 = int(input("masukan jumlah penduduk 9 thn yang lalu "+" :"))
print( 10*"-")
y3 = int(input("masukan jumlah penduduk 8 thn yang lalu "+" :"))
y4 = int(input("masukan jumlah penduduk 7 thn yang lalu "+" :"))
print( 10*"-")
y5 = int(input("masukan jumlah penduduk 6 thn yang lalu "+" :"))
y6 = int(input("masukan jumlah penduduk 5 thn yang lalu "+" :"))
print( 10*"-")
y7 = int(input("masukan jumlah penduduk 4 thn yang lalu "+" :"))
y8 = int(input("masukan jumlah penduduk 3 thn yang lalu "+" :"))
print( 10*"-")
y9 = int(input("masukan jumlah penduduk 2 thn yang lalu "+" :"))
y10 = int(input("masukan jumlah penduduk 1 thn yang lalu "+" :"))
print( 50*"-")
print("")
print("")


n=10

x21=x1*x1
x22=x2*x2
x23=x3*x3
x24=x4*x4
x25=x5*x5
x26=x6*x6
x27=x7*x7
x28=x8*x8
x29=x9*x9
x20=x10*x10

yx1= x1*y1
yx2= x2*y2
yx3= x3*y3
yx4= x4*y4
yx5= x5*y5
yx6= x6*y6
yx7= x7*y7
yx8= x8*y8
yx9= x9*y9
yx10= x10*y10

zx= x1+x2+x3+x4+x5+x6+x7+x8+x9+x10
zy= y1+y2+y3+y4+y5+y6+y7+y8+y9+y10
zx2= x21+x22+x23+x24+x25+x26+x27+x28+x29+x20
zxy= yx1+yx2+yx3+yx4+yx5+yx6+yx7+yx8+yx9+yx10

zx22=zx*zx

b1=(n*zxy)-(zx*zy)
b2=(n*zx2)-zx22
b=b1/b2

a1=zy/n
a2=b*(zx/n)
a=a1-a2

f=(a)+b*x
j=f-y10

input("enter untuk melihat HASIL")
print( 50*"-")
print( "Di perkirakan jumlam penduduk di tahun ",x, " bertambah ",j," penduduk")
print("jadi prediksi penduduk tahun ",x," sejumlah : ", f ," penduduk")
print( 50*"-")

input("enter untuk melihat tabel")


print( 61*"-")
print("| "," NO ","|  tahun ","|  penduduk  ","|     X2    ","|     XY    ","   |")
print( 61*"-")
print("| "," 1 ","    ",x1,"      ",y1,"        ",x21,"        ",  yx1)
print("| "," 2 ","    ",x2,"      ",y2,"        ",x22,"        ",  yx2)
print("| "," 3 ","    ",x3,"      ",y4,"        ",x23,"        ",  yx3)
print("| "," 4 ","    ",x4,"      ",y4,"        ",x24,"        ",  yx4)
print("| "," 5 ","    ",x5,"      ",y5,"        ",x25,"        ",  yx5)
print("| "," 6 ","    ",x6,"      ",y6,"        ",x26,"        ",  yx6)
print("| "," 7 ","    ",x7,"      ",y7,"        ",x27,"        ",  yx7)
print("| "," 8 ","    ",x8,"      ",y8,"        ",x28,"        ",  yx8)
print("| "," 9 ","    ",x9,"      ",y9,"        ",x29,"        ",  yx9)
print("| "," 10 ","    ",x10,"     ",y10,"       ",x20,"        ",  yx10)
print( 61*"-")
print("| ","Sigma","    ",zx,"     ",zy,"       ",zx2,"       ",  zxy)
print( 61*"-")






