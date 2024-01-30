datos=[18	,35,	22,	41,	35,	68,	30,	30,	30	,46,	42,	32,	30,	16,	28,	35,	35,	35,	44,	44,	44,	39,	44,	61,	55,	32,	32,	28,28,	29,	25,	25,	28,	54,	53,	35,	60,	35,	35,	35,	64,	35,	35,	34,	22,	44,	17,	16,	46,	46,	27,	25,	46,	47,	46,	35,39,	59,	59,	32,	32,	28,	35,	27,	31,	30,	32,	61,	35,	54,	57,	35,	56,	44,	58,	41,	42,	44,	30,	40,	46,	46,	50,	49,50,	36,	41,	29]
x= 2
while x > 1:
    
    inferior=int(input("Ingrese el intervalo inferior: "))
    superior=int(input("Ingrese el intervalo superior: "))
    w=0
    for n in datos:
        if (n < superior and n>=inferior):
            w=w+1;
            print(n)
    print("-----------------")
    print("total")
    print(w)