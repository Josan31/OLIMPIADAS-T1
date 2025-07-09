# Muestra el título en mayúsculas
print("Registro de productos y análisis básico".upper())

# Crea la lista 'productos' con 4 frutas ingresadas por el usuario (con la primera letra en mayúscula)
productos = [
    input("Ingresa la primera fruta: ").capitalize(),
    input("Ingresa la segunda fruta: ").capitalize(),
    input("Ingresa la tercera fruta: ").capitalize(),
    input("Ingresa la última fruta: ").capitalize()
]
print(f"Dada la lista {productos} se harán los procedimientos.")

# Crea la lista 'precios' con 3 precios ingresados por el usuario
precios = [
    int(input("Ingresa el primer precio: ")),
    int(input("Ingresa el segundo precio: ")),
    int(input("Ingrese el último precio: "))
]
print(f"Dada la lista con los precios {precios} se harán los procedimientos.")

# Paso 1: si "Pera" está en productos, agregar "Mango"
print("\nPaso N°1")
if "Pera" in productos:
    productos.append("Mango")
    print(f"Pera está en la lista inicial productos, por lo cuál se agrega Mango. Tu lista actualizada es: {productos}")
else:
    print("Pera NO está en productos")

# Paso 2: si 1800 está en precios, agregar 2000
print("\nPaso N°2")
if 1800 in precios:
    precios.append(2000)
    print(f"El valor 1800 está en precios, se agrega 2000. Lista actualizada: {precios}")
else:
    print("1800 no está en precios")
    
# Paso 3: si banano está en lista productos, lo elimino
print("\nPaso N°3")
if "Banano" in productos:
    productos.remove("Banano")
    print(f"Banano está en tu lista de productos, por lo cuál se elimará. Tu lista actualizada es: {productos}")
else:
    print("Banano NO está en la lista productos")

# Paso 4: si productos tiene exactamente 4 elementos, eliminar el primero
print("\nPaso N°4")
if len(productos) == 4:
    productos.pop(0)
    print(f"Se eliminó el primer producto. Lista actualizada: {productos}")
else:
    print("La lista productos no tiene 4 elementos")

# Paso 5: si 1500 está en precios, reemplazarlo por 1600
print("\nPaso N°5")
if 1500 in precios:
    precios.remove(1500)
    precios.append(1600)
    print(f"Se reemplazó 1500 por 1600. Lista actualizada: {precios}")
else:
    print("1500 no está en la lista precios")

# Paso 6: crear lista 'oferta' con los dos primeros productos
print("\nPaso N°6")
oferta = [productos[0], productos[1]]
print(f"Nueva lista oferta: {oferta}")

# Paso 7: crear lista 'altos_precios' con los dos últimos precios
print("\nPaso N°7")
altos_precios = [precios[1], precios[2]]
print(f"Nueva lista altos_precios: {altos_precios}")

# Paso 8: si "Mango" está en productos, crear tupla con Mango y 2000
print("\nPaso N°8")
if "Mango" in productos:
    tupla1 = ("Mango", 2000)
    print(f"Tupla creada: {tupla1}")
else:
    print("Mango no está en productos")

# Paso 9: si "Manzana" está en oferta, agregar "Descuento" a oferta
print("\nPaso N°9")
if "Manzana" in oferta:
    oferta.append("Descuento")
    print(f"Se agregó 'Descuento' a oferta: {oferta}")
else:
    print("Manzana no está en la lista oferta")

# Paso 10: si "Descuento" está en oferta, crear diccionario 'informe'
print("\nPaso N°10")
if "Descuento" in oferta:
    informe = {"producto": "Manzana", "precio_original": 1600, "descuento": True}
    print(f"Diccionario creado: {informe}")
else:
    print("Descuento no está en la lista oferta")

# Paso 11: si el diccionario 'informe' existe, agregar clave 'Vigencia'
print("\nPaso N°11")
if 'informe' in locals():  # Verifica si informe fue creado
    informe["Vigencia"] = "30 días"
    print(f"Diccionario actualizado con vigencia: {informe}")
else:
    print("El diccionario no existe")

# Paso 12: si precios tiene más de 3 elementos, eliminar el último
print("\nPaso N°12")
if len(precios) > 3:
    precios.pop()
    print(f"Se eliminó el último precio. Lista actualizada: {precios}")
else:
    print("La lista precios no tiene más de 3 elementos")

# Paso 13: si "Piña" no está en productos, agregarla
print("\nPaso N°13")
if "Piña" not in productos:
    productos.append("Piña")
    print(f"Piña fue agregada. Lista actualizada: {productos}")
else:
    print("Piña ya está en productos")

# Paso 14: mostrar las listas, tupla y diccionario finales
print("\nPaso N°14")
print(f"Lista final de productos: {productos}")
print(f"Lista final de precios: {precios}")
print(f"Lista final de oferta: {oferta}")
print(f"Lista final de altos_precios: {altos_precios}")
print(f"Tupla final: {tupla1 if 'tupla1' in locals() else 'No fue creada'}")
print(f"Diccionario final: {informe if 'informe' in locals() else 'No fue creado'}")
