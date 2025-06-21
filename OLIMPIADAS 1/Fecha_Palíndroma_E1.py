print("Determinar si una fecha es palíndroma".upper())

dia = int(input("Ingrese el dia (1-31)"))
mes = int(input("Ingrese el mes (1-12)"))
año = int(input("Ingrese el año (por ejemplo 2020)"))
fecha = f"{dia:02d}{mes:02d}{año:04d}"

if fecha == fecha[::1]:
    print(f"Tu fecha {fecha} es palíndroma")
else: print(f"Tu fecha {fecha} NO es palíndroma")
