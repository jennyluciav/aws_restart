print("Inicio de condicionales")
userReply = input("¿Necesita enviar un paquete? (Escriba sí o no) ")

if userReply == "si":
    print("Podemos ayudarlo con su paquete")
else:
    print("Vuelva cuando necesite enviar un paquete. Gracias")

userReply = input("¿Le gustaría comprar sellos, un sobre o hacer una copia? (Escriba sellos, sobre o copia)")

if userReply == "sellos":
    print("Tenemos muchos diseños de sellos para elegir")
elif userReply == "sobre":
    print("Tenemos muchos tamaños de sobres para elegir.")
elif userReply == "copia":
    print("¿Cuántas copias le gustaría? (Escriba un número)")
else:
    print("Gracias, por favor venga de nuevo.")
    
print("Fin de condicionales")
