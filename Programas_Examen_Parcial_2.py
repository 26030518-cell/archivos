# Programas en orden de aparición — Examen Parcial 2
# Cada tema incluye el ejemplo y un programa extra.

#====================================================================
# 01. Tipos de datos — ejemplo
#====================================================================
# Tipos de datos básicos
nombre = "Leo"
edad = 18
estatura = 1.72
es_estudiante = True
print("Nombre:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Es estudiante?:", es_estudiante)


#====================================================================
# 01 EXTRA. Tipos de datos — ficha de herramienta
#====================================================================
herramienta = "Multímetro"
precio = 350.50
cantidad = 4
disponible = True
print("Herramienta:", herramienta)
print("Precio:", precio)
print("Cantidad:", cantidad)
print("Disponible:", disponible)


#====================================================================
# 02. Números — ejemplo
#====================================================================
a = 10
b = 3
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Residuo:", a % b)
print("Potencia:", a ** b)


#====================================================================
# 02 EXTRA. Conversión de temperatura
#====================================================================
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperatura en Fahrenheit:", fahrenheit)


#====================================================================
# 03. Strings — ejemplo
#====================================================================
nombre = "Leonardo"
apellido = "Silva"
print("Nombre completo:", nombre + " " + apellido)
print("Mayúsculas:", nombre.upper())
print("Minúsculas:", nombre.lower())
print("Cantidad de letras:", len(nombre))
print("Primera letra:", nombre[0])


#====================================================================
# 03 EXTRA. Crear un correo
#====================================================================
nombre = input("Nombre: ").strip().lower()
apellido = input("Apellido: ").strip().lower()
correo = nombre + "." + apellido + "@ejemplo.com"
print("Correo:", correo)


#====================================================================
# 04. Booleanos y operadores lógicos — ejemplo
#====================================================================
edad = 18
tiene_identificacion = True
if edad >= 18 and tiene_identificacion:
    print("Puede ingresar")
else:
    print("No puede ingresar")


#====================================================================
# 04 EXTRA. Verificar aprobación
#====================================================================
calificacion = float(input("Calificación: "))
asistencia = input("¿Cumplió asistencia? (si/no): ").lower()
if calificacion >= 6 and asistencia == "si":
    print("Aprobado")
else:
    print("No aprobado")


#====================================================================
# 05. None — ejemplo
#====================================================================
resultado = None
print("Valor inicial:", resultado)
resultado = "Terminado"
print("Valor final:", resultado)


#====================================================================
# 05 EXTRA. Buscar un producto
#====================================================================
buscado = input("Producto que buscas: ").lower()
producto_encontrado = None
if buscado == "sensor":
    producto_encontrado = "Sensor de proximidad"
if producto_encontrado is None:
    print("Producto no encontrado")
else:
    print("Encontrado:", producto_encontrado)


#====================================================================
# 06. Operadores aritméticos — ejemplo
#====================================================================
print("Suma:", 5 + 3)
print("Resta:", 5 - 3)
print("Multiplicación:", 5 * 3)
print("División:", 5 / 3)
print("Residuo:", 10 % 3)
print("Potencia:", 2 ** 3)


#====================================================================
# 06 EXTRA. Costo de compra
#====================================================================
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva
print("Subtotal:", subtotal)
print("IVA:", iva)
print("Total:", total)


#====================================================================
# 07. Operadores de asignación — ejemplo
#====================================================================
cantidad = 10
print("Inicial:", cantidad)
cantidad += 5
print("Después de += 5:", cantidad)
cantidad -= 2
print("Después de -= 2:", cantidad)
cantidad *= 2
print("Después de *= 2:", cantidad)
cantidad /= 2
print("Después de /= 2:", cantidad)


#====================================================================
# 07 EXTRA. Acumular puntos
#====================================================================
puntos = 0
puntos += int(input("Puntos de la primera ronda: "))
puntos += int(input("Puntos de la segunda ronda: "))
puntos += int(input("Puntos de la tercera ronda: "))
print("Puntos totales:", puntos)


#====================================================================
# 08. Operadores lógicos — ejemplo
#====================================================================
edad = 18
tiene_identificacion = True
if edad >= 18 and tiene_identificacion:
    print("Acceso permitido")
if edad < 18 or not tiene_identificacion:
    print("Acceso denegado")


#====================================================================
# 08 EXTRA. Revisar rango
#====================================================================
medida = float(input("Ingresa la medida: "))
if medida >= 10 and medida <= 20:
    print("Medida dentro del rango")
else:
    print("Medida fuera del rango")


#====================================================================
# 09. Entrada de datos — ejemplo
#====================================================================
nombre = input("¿Cuál es tu nombre? ")
edad = input("¿Cuántos años tienes? ")
print("Hola,", nombre)
print("Tu edad es:", edad)


#====================================================================
# 09 EXTRA. Datos de un componente
#====================================================================
componente = input("Nombre del componente: ")
voltaje = input("Voltaje de operación: ")
print("Componente:", componente)
print("Voltaje:", voltaje, "V")


#====================================================================
# 10. Conversión de tipos (casting) — ejemplo
#====================================================================
numero_texto = "42"
numero_entero = int(numero_texto)
numero_decimal = float("3.14")
print("Entero:", numero_entero)
print("Decimal:", numero_decimal)
print("Suma:", numero_entero + numero_decimal)
print("Redondeo:", round(numero_decimal, 1))


#====================================================================
# 10 EXTRA. Promedio con casting
#====================================================================
cal1 = float(input("Primera calificación: "))
cal2 = float(input("Segunda calificación: "))
cal3 = float(input("Tercera calificación: "))
promedio = (cal1 + cal2 + cal3) / 3
print("Promedio:", round(promedio, 2))


#====================================================================
# 11. Colecciones — ejemplo
#====================================================================
lista = ["motor", "sensor", "cable"]
tupla = ("rojo", "verde", "azul")
conjunto = {"A", "B", "C"}
diccionario = {"nombre": "Motor", "cantidad": 3}
print("Lista:", lista)
print("Tupla:", tupla)
print("Conjunto:", conjunto)
print("Diccionario:", diccionario)


#====================================================================
# 11 EXTRA. Colecciones para inventario
#====================================================================
productos = ["Tornillos", "Sensores", "Cables"]
ubicaciones = ("Estante A", "Estante B")
categorias = {"mecánica", "electrónica"}
inventario = {"Tornillos": 100, "Sensores": 8, "Cables": 25}
print("Productos:", productos)
print("Ubicaciones:", ubicaciones)
print("Categorías:", categorias)
print("Inventario:", inventario)


#====================================================================
# 12. Listas — ejemplo
#====================================================================
alumnos = ["Ana", "Luis", "Pedro"]
print("Lista completa:", alumnos)
print("Primer alumno:", alumnos[0])
for alumno in alumnos:
    print(alumno)


#====================================================================
# 12 EXTRA. Lista de herramientas
#====================================================================
herramientas = ["Pinzas", "Desarmador", "Multímetro"]
herramientas.append("Taladro")
print("Herramientas:", herramientas)
print("Cantidad:", len(herramientas))


#====================================================================
# 13. Operaciones con listas — ejemplo
#====================================================================
numeros = [4, 2, 8, 1]
numeros.append(6)
print("Después de agregar:", numeros)
numeros.remove(2)
print("Después de eliminar el 2:", numeros)
numeros.sort()
print("Ordenada:", numeros)
print("Longitud:", len(numeros))


#====================================================================
# 13 EXTRA. Ordenar calificaciones
#====================================================================
calificaciones = [8.5, 7.0, 9.2, 6.8]
calificaciones.append(float(input("Agrega otra calificación: ")))
calificaciones.sort()
print("Calificaciones ordenadas:", calificaciones)
print("Mayor:", max(calificaciones))
print("Menor:", min(calificaciones))


#====================================================================
# 14. Tuplas — ejemplo
#====================================================================
periodo = ("Agosto", "Diciembre", 2026)
print("Periodo:", periodo)
print("Mes inicial:", periodo[0])
print("Mes final:", periodo[1])
print("Año:", periodo[2])


#====================================================================
# 14 EXTRA. Coordenadas con tupla
#====================================================================
punto = (5, 8)
print("Coordenada X:", punto[0])
print("Coordenada Y:", punto[1])


#====================================================================
# 15. Conjuntos — ejemplo
#====================================================================
frutas = {"manzana", "naranja", "manzana", "pera"}
print("Frutas sin repetir:", frutas)
frutas.add("uva")
print("Después de agregar uva:", frutas)
frutas.discard("pera")
print("Después de quitar pera:", frutas)


#====================================================================
# 15 EXTRA. Piezas sin repetir
#====================================================================
piezas = set()
piezas.add("tornillo")
piezas.add("tuerca")
piezas.add("tornillo")
print("Tipos de piezas:", piezas)
print("Tipos diferentes:", len(piezas))


#====================================================================
# 16. Diccionarios — ejemplo
#====================================================================
producto = {"nombre": "Sensor", "precio": 120.50, "cantidad": 10}
print("Producto:", producto["nombre"])
print("Precio:", producto["precio"])
print("Cantidad:", producto["cantidad"])


#====================================================================
# 16 EXTRA. Ficha de alumno con diccionario
#====================================================================
alumno = {
    "nombre": input("Nombre del alumno: "),
    "grupo": input("Grupo: "),
    "calificacion": float(input("Calificación: "))
}
print("Ficha del alumno:")
for clave, valor in alumno.items():
    print(clave, ":", valor)


#====================================================================
# 17. Break y continue — ejemplo
#====================================================================
for numero in range(1, 6):
    if numero == 3:
        break
    print("Break:", numero)

for numero in range(1, 6):
    if numero == 3:
        continue
    print("Continue:", numero)


#====================================================================
# 17 EXTRA. Encontrar número con break y continue
#====================================================================
for numero in range(1, 50):
    if numero % 2 == 0:
        continue
    if numero % 7 == 0:
        print("Primer múltiplo impar de 7:", numero)
        break


#====================================================================
# 18. Práctica final — promedio de tres calificaciones
#====================================================================
nombre = input("Nombre del alumno: ")
calificaciones = [
    float(input("Primera calificación: ")),
    float(input("Segunda calificación: ")),
    float(input("Tercera calificación: "))
]
promedio = sum(calificaciones) / len(calificaciones)
print("\nNombre:", nombre)
print("Calificaciones:", calificaciones)
print("Promedio:", round(promedio, 2))
if promedio >= 6.0:
    print("Resultado: Aprobó")
else:
    print("Resultado: Reprobó")


#====================================================================
# 18 EXTRA. Calculadora de compra
#====================================================================
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad comprada: "))
total = precio * cantidad
print("Producto:", producto)
print("Cantidad:", cantidad)
print("Total a pagar: $", round(total, 2))


