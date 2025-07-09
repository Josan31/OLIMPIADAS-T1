# Muestra un título en mayúsculas
print("Determinar si una fecha es palíndroma".upper())

# Solicita al usuario el día, mes y año como números enteros
dia = int(input("Ingrese el dia (1-31)"))
mes = int(input("Ingrese el mes (1-12)"))
año = int(input("Ingrese el año (por ejemplo 2020)"))

# Formatea la fecha como un string en el formato DDMMYYYY (dos dígitos para día y mes, cuatro para año)
fecha = f"{dia:02d}{mes:02d}{año:04d}"

# Verifica si la fecha es igual a su reverso (si es un palíndromo)
if fecha == fecha[::-1]:
    print(f"Tu fecha {fecha} es palíndroma")
else:
    print(f"Tu fecha {fecha} NO es palíndroma")
