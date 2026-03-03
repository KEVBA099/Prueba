def saludo(nombre,apellido,edad):
    return f"Hola {nombre} {apellido}, tienes {edad} años, ¿Como te encuentras?"

valor = input("Escribe tu nombre: ")
valor2 = input("Escrino tu apellido: ")
valor3 = int(input("Escribe tu edad: "))
print(saludo(valor,valor2,valor3))