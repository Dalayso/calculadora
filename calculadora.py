
# creando repositorio de calculadora con git
# calculadora

print("\n○ calculadora virtual\n")

opción = input("""\n•Ingrese una opción para selecccionar una operacion:
\n-1》sumar\n
-2》restar\n
-3》multiplicar\n
-4》dividir\n--
""")

while opción >= "1" and opción <= "4":
    num1 = input("\nIngrese el primer numero\n")
    num2 = input("\nIngrese el segundo numero\n")
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        if opción == "1":
            resultado = num1 + num2
            print(f"El resultado es: {resultado}")
            break
        elif opción == "2":
            resultado = num1 - num2
            print(f"El resultado es: {resultado}")
            break
        elif opción == "3":
            resultado = num1 * num2
            print(f"El resultado es: {resultado}")
            break
        elif opción == "4":
            try:
                resultado = num1 / num2
                resultado = round(resultado,2)
                print(f"El resultado es: {resultado}")
            except ZeroDivisionError:
                    print("No se puede dividir por cero")
            break
    else:print("Ingrese solo numeros")
    continue
else:
    print("Ingrese una opcion correcta")