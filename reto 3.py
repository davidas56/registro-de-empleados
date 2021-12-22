for i in range(4):
    usuario = input()
    contraseña = input()
    print(f'Usuario: {usuario}\nContraseña: {contraseña}')
    if usuario != "admin" or contraseña !="MisionTic2021":
        print('Credenciales incorrectas')
    if i == 3 :
        print('Has agotado la cantidad de intentos, por favor inicie de nuevo el programa')
    if usuario == 'admin' and contraseña == "MisionTic2021":
        break
nombres=""
visitantes=""
while usuario == "admin" and contraseña =="MisionTic2021":
 print('\n------Menú de registro de personal-----\n1. Registrar ingreso de empleado.\n2. Ver empleados ingresados.\n3. Registrar ingreso de visitantes.\n4. Ver visitantes ingresados.\n\n0. Salir')
 b=int(input())
 print(f'\nIngresa un número válido de opción del menú: {b}')
 while b > 4 or b < 0:
    print('Por favor ingresa una opción válida')
    break
 if b==0:
    print("¡Hasta luego!")
    break
 while b==1:
    nombre1=input()
    print(f"Ingresa el nombre del empleado (Si no deseas agregar más, oprime la tecla SALIR): {nombre1}")
    if nombre1 != "SALIR":  
        nombres=nombres+nombre1+","
    if nombre1 == "SALIR":
        break
 while b==2:
     print(f"Los empleados registrados son: {nombres}")
     break
 while b==3:
    nombre1=input()
    print(f"Ingresa el nombre del visitante (Si no deseas agregar más, digite SALIR): {nombre1}")
    if nombre1 != "SALIR":  
        visitantes=visitantes+nombre1+","
    if nombre1 == "SALIR":
        break
 while b==4:
     print(f"Los visitantes registrados son: {visitantes}")
     break
