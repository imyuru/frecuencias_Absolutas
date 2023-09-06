datos=[1000,	1110,	1010,	1070,	1030,	1000,
1150,	990,	1090,	1080,	1150,	1200,
1050,	1030,	1120,	1050,	1030,	1150,
1230,	1170,	1180,	1110,	1160,	1100,
1100,	1060,	1130,	1105,	935,	1210]

inferior=int(input("Ingrese el intervalo inferior"))
superior=int(input("Ingrese el intervalo superior"))
w=0
for n in datos:
     if (n < superior and n>=inferior):
        w=w+1;
        print(n)
print("-----------------")
print("total")
print(w)