import comandos

def menu():
    op=0
    salir=8
    while(op!=salir): #Mostrar el menu
        print("""  
        SIMPLEQL
-------------------------
     Menu de inicio
-------------------------    
    1. Cargar
    2. Seleccionar
    3. Maximo
    4. Minimo
    5. Suma
    6. Cuenta
    7. Reportar
    8. Salir
        """)
        op = int (input('Opcion elegida: ')) #Ingresar Opcion

        if op==1:
            comandos.Cargar()
        if op==2:
            comandos.Seleccionar() 
        if op==3:
            comandos.Maximo() 
        if op==4:
            comandos.Minimo()
        if op==5:
            comandos.Suma()
        if op==6:
            comandos.Contar()
        if op==7:
            comandos.Reportar() 
        if op==8:
            print('Gracias por utilizar SIMPLEQL') 
        if op>=9:
            print('Error: Opcion Invalida')                        

menu()