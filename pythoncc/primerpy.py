import csv
import json
import os

cwd = os.getcwd()
print("Directorio actual: ", cwd)
txt = [f for f in os.listdir('.') if f.endswith('.txt')]
print("los archivos txt: ", txt)













# with open ('products.json', mode='r') as file: 
#     products = json.load(file)
# for product in products:
#     print(f"Producto: {product['name']}, Precio: {product['price']}")














# with open('products.csv', mode='r') as file:
#     cvs_reader = csv.DictReader(file)
#     for row in cvs_reader:
#         print(row)

#mostrar informacion por columnas
# with open('products.csv', mode='r') as file:
#     cvs_reader = csv.DictReader(file)
#     for row in cvs_reader:
#         print(f"Producto:  {row['name']}, Precio: {row['price']}")

# new_product = {
#     'name': 'wireless charger',
#     'price': 75,
#     'quantity': 100,
#     'brand': 'chargermaster',
#     'category':'Accessories',
#     'entry_date': '2024-07-01'
# }        
# with open('products.csv', mode='a', newline='') as file:
#     file.write('\n')
#     csv_writer = csv.DictWriter(file,fieldnames=new_product.keys())  
#     csv_writer.writerow(new_product)









# with open('cuento.txt', 'a') as file:
#     file.write("\n\nLa cabra es messiiiii")

# # with open('cuento.txt', 'r') as file:
# #     for lineas in file:
# #         print(lineas.strip())    

# with open('cuento.txt', 'r') as file:
#     contenido = file.read()
#     print(contenido)




# def suma(a,b):
#     return a+b;
# def resta(a,b):
#     return a-b;
# def multiplicacion(a,b):
#     return a*b;
# def division(a,b):
#     return a/b;


# while True:
#     print("1:suma");
#     print("2:resta");
#     print("3:multiplicacion");
#     print("4:division");
#     print("5:salir");
#     eleccion = int(input("ingrese el numero que queres: "))
#     if eleccion == 5:
#         print('saliste')
#         break
#     if eleccion in [1,2,3,4]:
#         num1 = float(input("n1"))
#         num2 = float(input("n2"))
#         if eleccion == 1:
#             print("suma: ", suma(num1,num2))
#         if eleccion == 2:
#             print("resta: ", resta(num1,num2))
#         if eleccion == 3:
#             print("multi: ", multiplicacion(num1,num2))
#         if eleccion == 4:
#             print("division: ", division(num1,num2))        
#     else:
#         print("que pedo?")
#         break;




# import random

# def adivina_numero():
#     print("¡Bienvenido a Adivina el Número!")
#     print("Estoy pensando en un número entre 1 y 50...")

#     numero_secreto = random.randint(1, 50)
#     intentos = 0

#     while True:
#         try:
#             intento = int(input("Ingresa tu número: "))
#             intentos += 1

#             if intento < numero_secreto:
#                 print("Es más alto...")
#             elif intento > numero_secreto:
#                 print("Es más bajo...")
#             else:
#                 print(f"¡Correcto! El número era {numero_secreto}.")
#                 print(f"Te tomó {intentos} intentos.")
#                 break
#         except ValueError:
#             print("Ingresa un número válido.")

# # Ejecutar el juego
# adivina_numero()