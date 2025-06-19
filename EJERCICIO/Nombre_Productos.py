print("Registro de productos y análisis básico")

# creo las dos listas inicales 
productos = [input("Ingresa la primera fruta: "), input("Ingresa la segunda fruta: "), input("Ingresa una última nota")]
precios = [int(input("Ingresa el primer precio: ")), int(input("Ingresa el segundo precio: ")), int(input("Ingrese el último precio: "))]

# Paso 1: si pera está agrego Mango
if "Pera" in productos:
    productos.append("Mango")
    print(f"La lista actualizada es: {productos}")
          
# Paso 2: si 1800 está, agrego 2000
if 1800 in precios:
    precios.append(2000)
    print(f"tu lista actualizada es: {precios}")
    
# Paso 3: si banano está, lo elimino
if "Banano" in productos:
    productos.remove("Banano")
    print(f"tu lista actualizada es: {productos}")

# Paso 4: si la lista productos tiene 4 elementos 
if len(productos) == 4:
    productos.remove("Manzana")
    print(f"La lista actualizada es: {productos}")
    
# Paso 5: si el precio 1500 está, lo reemplazo por 1600
if 1500 in precios:
    precios.remove(1500)
    precios.append(1600)
    print(f"La lista actualizada es: {precios}")

# Paso 6: crear lista llamada oferta
oferta = ["Manzana", "Banano"]

# Paso 7: crear lista llamada altos_precios
altos_precios = [1000, 1800]

# Paso 8: si mango está en la lista creo una tupla
if "Mango" in productos:
    tupla1 = ("Mango", 2000)

# Paso 9: si manzana está en la varibale oferta agrego la palabra Descuento al final de la lista
if "Manzana" in oferta:
    oferta.append("Descuento")
    print(f"La palabra está en la lista: {oferta} ")

# Paso 10: 
if "Descuento" in oferta:
    informe = {"producto": "Manzana", "precio_original": 1600, "descuento": True}

# Paso 10: si Descuento está en la lista pferta creo un diccionario con claves
if informe 
    



    
