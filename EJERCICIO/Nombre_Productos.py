print("Registro de productos y análisis básico".upper())

# creo las dos listas inicales 
productos = [input("Ingresa la primera fruta: ").capitalize(), input("Ingresa la segunda fruta: ").capitalize(), input("Ingresa la tercera fruta: ").capitalize(), input("Ingresa la última fruta: ").capitalize()]
print(f"Dada la lista {productos} se haran los procedimientos.")
precios = [int(input("Ingresa el primer precio: ")), int(input("Ingresa el segundo precio: ")), int(input("Ingrese el último precio: "))]
print(f"Dado la lista con los precios {precios} se harán los procedimientos.")

# # Paso 1: si "pera" está en productos agrego Mango
# print("\nPaso N°1")
# if "Pera" in productos:
#     productos.append("Mango")
#     print(f"Pera está en la lista inicial productos, por lo cuál se agrega Mango. Tu lista actualizada es: {productos}")
# else:
#     print("Pera NO está en productos")
          
# # Paso 2: si 1800 está en precios agrego 2000
# print("\nPaso N°2")
# if 1800 in precios:
#     precios.append(2000)
#     print(f"En tu lista de los precios se encuentra el valor 1800, por lo cuál se agrega el valor de 2000. Tu lista actualizada es: {precios}")
# else:
#     print("El valor 1800 no está en la lista precios")
    
# # Paso 3: si banano está en lista productos, lo elimino
# print("\nPaso N°3")
# if "Banano" in productos:
#     productos.remove("Banano")
#     print(f"Banano está en tu lista de productos, por lo cuál se elimará. Tu lista actualizada es: {productos}")
# else:
#     print("Banano NO está en la lista productos")

# # Paso 4: si la lista productos tiene 4 elementos 
# print("\nPaso N°4")
# if len(productos) == 4:
#     productos.pop(0)
#     print(f"Tu lista de productos tiene 4 elementos, por lo cuál se eliminará el primero. Tu lista actualizada es: {productos}")
# else:
#     print("La lista productos no tiene 4 elementos")
    
# # Paso 5: si el precio 1500 está, lo reemplazo por 1600
# print("\nPaso N°5")
# if 1500 in precios:
#     precios.remove(1500)
#     precios.append(1600)
#     print(f"El precio 1500 se encuentra en la lista, por lo cuál será reemplazado por 1600. La lista actualizada es: {precios}")
# else:
#     print("1500 no está en la lista precios")

# # Paso 6: crear lista llamada oferta con los dos primeros elementos de la lista productos
# print("\nPaso N°6")
# oferta = [productos[0], productos[1]]
# print(f"La nueva lista con los dos primeros elementos de la lista productos es: {oferta}")

# # Paso 7: crear lista llamada altos_precios con los dos últimos precios de la lista
# print("\nPaso N°7")
# altos_precios = [precios[1], precios[2]]
# print(f"La nueva lista con los dos últimos precios de la lista es: {altos_precios}")

# # Paso 8: si mango está en la lista creo una tupla
# print("\nPaso N°8")
# if "Mango" in productos:
#     tupla1 = ("Mango", 2000)
#     print(f"Mango está en la lista productos, por lo cuál creo la siguiente tupla: {tupla1}")
# else:
#     print("Mango no está en la lista productos")

# # Paso 9: si manzana está en oferta agrego la palabra Descuento al final de la lista
# print("\nPaso N°9")
# if "Manzana" in oferta:
#     oferta.append("Descuento")
#     print(f"La palabra Descuento se agregó a la lista: {oferta}")
# else:
#     print("Manzana no está en la lista oferta")

# # Paso 10: si Descuento está en oferta creo un diccionario llamado informe
# print("\nPaso N°10")
# if "Descuento" in oferta:
#     informe = {"producto": "Manzana", "precio_original": 1600, "descuento": True}
#     print(f"La palabra Descuento estaba en la lista oferta, por lo cuál se crea el siguiente diccionario: {informe}")
# else:
#     print("Descuento no está en la lista oferta")

# Paso 10: si Descuento está en la lista pferta creo un diccionario con claves

    



    
