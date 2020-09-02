import json
import re
import dominate
from dominate.tags import *
import webbrowser
archivos=""
ArCorrectos=[]
Cumplecondi=[]
condi=[]

def Cargar(): #cargar objetos
    print("""
    INTRUCCIONES:
    Para cargar los archivos json deseados debe poner el comando Cargar seguido de los archivos que desea cargar separados por coma:
    (Ejemplo: Cargar archivoN.json, archivoM.json). 
    """)
    cargados=input() #Escribe los archivos que desea cargar
    cargados=cargados.lower() #Case Insensitive
    cargados=cargados.replace('cargar','') #Quita la palabra cargar
    cargados=cargados.replace(',',' ') #Quita las comas
    archivos=cargados.split() #Ingresa los archivos a una lista
    print('Opcion 1 cargar')
    a=""
    for Ar in archivos: #Recorre la lista de archivos
        a = a + Ar
        print(Ar)
        try: #Los lee para ver si existe
            with open(Ar) as info:
                prueba = json.loads(info.read())
            print(prueba)    #Si lo lee es porque si existe
            ArCorrectos.append(Ar) #Agrega a una ueva lista con los que si existen
        except:
            print('ERROR: Archivo no encontrado:', Ar) #Error que el arvhivo no existe y los descarta 
    print(ArCorrectos)

def Seleccionar(): #Seleccionar registros o atributos dentro de los archivos
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l+ Listado +" "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder elegir los registros o atributos deseados debera escribir Seleccionar seguido de los registros y atributos 
    separados por coma luego la palabre DONDE seguido de condicion. 
    *(EJEMPLO: SELECCIONAR nombre, edad DONDE edad=10)*. Si desea ver todos el comando es SELECCIONAR*
    """)
    a=""
    reg=""
    
    seleccionados=input() #Ingresar lo que se desea seleccionar
    seleccionados=seleccionados.lower() #Case Insensitive
    seleccionados=seleccionados.replace('seleccionar','') #Borrar el seleccionar
    seleccionados=seleccionados.replace(',',' ') #Cambiar comas por espacios
    seleccionados=seleccionados.replace('donde','') #Quitar la palabra donde
    seleccionados=seleccionados.replace('\'','')
    registros=re.split('=',seleccionados) 
    regcero=registros[0].split()
    registros.append(regcero)
    print(registros) 
    del registros[0]
    print(registros)
    z=0
    for cero in regcero:
        z=z+1 
    condicion=regcero[z-1] 
    print(condicion)   
    del regcero[z-1]   
    print(regcero)
    try:
        if registros==[['*']]: #Para cuando se quiere ver lo que hay en todo el json
            print('Prueba de *')
            for Arco in ArCorrectos: #Recorre la lista de correctos
             a = a + Arco +" " 
             print('------------------------')
             print('      ',Arco)
             print('------------------------')
             with open(Arco,'r') as info: #Lee el archivo json
                prueba = json.loads(info.read())
                print(json.dumps(prueba,indent=4))
        else:    
            for Arco in ArCorrectos: #Recorre la lista de correctos
                condispedidas=[]
                valorcondis=[]
                a = a + Arco
                print('------------------------')
                print('     ',Arco)
                print('------------------------')

                with open(Arco,'r') as info:  #Lee el archivo json
                    prueba = json.loads(info.read())
                    for p in prueba: 
                        obcondi=str(p.get(condicion)) #Obtiene el valor dentro del json que equivale al valor de la condicion y lo convierte a str
                        obcondi=obcondi.lower()
                        condint=registros[0] #Obtiene el valor de la condicion
                        if obcondi == condint: #No son iguales
                            for r in regcero: #Recorre los registros que quiere el usuario
                             reg=reg + r 
                             condispedidas.append(r) #Los mete en la lista de los registros pedidos
                             regs=p.get(r) #obtiene el valor de los registros pedidos
                             valorcondis.append(regs) #Los mete en la lista de los valores

                i=0
                while i<=len(condispedidas)-1:
                    print('{:^10}{:^10}'.format(condispedidas[i],valorcondis[i])) #Escribe la tabla
                    i+=1
                print('------------------------')
    except:
        print('ALGO SALIO MAL')

def Maximo():
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l + Listado + " "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder ver el valor maximo de un atributo escriba la palabra MAXIMO seguida del atributo.
    (SOLO ATRIBUTOS NUMERICOS)
    """)
    a=""
    maximo=input() #Ingresar lo que se desea maximo
    maximo=maximo.lower() #Case Insensitive
    maximo=maximo.replace('maximo','')
    maximo=maximo.replace(' ','')
    if maximo=='edad': #Maximo para edad
        for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaMax=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(maximo)
                    ListaMax.append(obcondi) #Agrega a una ueva lista con los que si existen
            mayor=ListaMax[0]
            for n in ListaMax:
                if n > mayor:
                    mayor = n
            print('La edad maxima es de: ',mayor)
            print('------------------------')
    elif maximo=='promedio': #Maximo para primedio
       for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaMax=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(maximo)
                    ListaMax.append(obcondi) #Agrega a una ueva lista con los que si existen
            mayor=ListaMax[0]
            for n in ListaMax:
                if n > mayor:
                    mayor = n
            print('El promedio maximo es de: ',mayor)
            print('------------------------')      
    else:
        print('Atributo invalida. Puede que no sea numerico o no exista')

def Minimo():
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l + Listado + " "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder ver el valor minimo de un atributo escriba la palabra MINIMO seguida del atributo.
    (SOLO ATRIBUTOS NUMERICOS)
    """)
    a=""
    minimo=input() #Ingresar lo que se desea minimo
    minimo=minimo.lower() #Case Insensitive
    minimo=minimo.replace('minimo','')
    minimo=minimo.replace(' ','')
    if minimo=='edad': #Minimo para edad
        for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaMin=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(minimo)
                    ListaMin.append(obcondi) #Agrega a una ueva lista con los que si existen
            menor=ListaMin[0]
            for n in ListaMin:
                if n < menor:
                    menor = n
            print('La edad minima es de: ',menor)
            print('------------------------')
    elif minimo=='promedio': #Minimo para primedio
        for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaMin=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(minimo)
                    ListaMin.append(obcondi) #Agrega a una ueva lista con los que si existen
            menor=ListaMin[0]
            for n in ListaMin:
                if n < menor:
                    menor = n
            print('La edad minima es de: ',menor)
            print('------------------------')    
    else:
        print('Atributo invalido. Puede que no sea numerico o no exista')
        
def Suma():
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l + Listado + " "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder ver la suma de un atributo escriba la palabra SUMA seguida del atributo.
    (SOLO ATRIBUTOS NUMERICOS)
    """)
    a=""
    suma=input() #Ingresar lo que se desea sumar
    suma=suma.lower() #Case Insensitive
    suma=suma.replace('suma','')
    suma=suma.replace(' ','')
    if suma=='edad': #Suma para edad
       for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaSuma=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(suma)
                    ListaSuma.append(obcondi) #Agrega a una ueva lista con los que si existen
            suma=0
            for i in ListaSuma:
                suma+=i
            print('La suma de la edad es de: ',suma)   
    elif suma=='promedio': #Suma para primedio
        for Ar in ArCorrectos: #Recorre la lista de archivos
            ListaSuma=[]
            a = a + Ar
            print('------------------------')
            print('      ',Ar)
            print('------------------------')
            with open(Ar) as info: #Lee el archivo json
                prueba = json.loads(info.read()) 
                for p in prueba: 
                    obcondi=p.get(suma)
                    ListaSuma.append(obcondi) #Agrega a una ueva lista con los que si existen
            suma=0
            for i in ListaSuma:
                suma+=i
            print('La suma de los promedios es de: ',suma) 
    else:
        print('Atributo invalido. Puede que no sea numerico o no exista')        

def Contar():
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l + Listado + " "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder ver la cantidad de registros dentro del archivo json debe escribir el comando CONTAR
    """)
    a=""
    contar=input() #Ingresar lo que se desea sumar
    contar=contar.lower() #Case Insensitive
    if contar=='contar':
        for Arco in ArCorrectos: #Recorre la lista de correctos
            ListaContar=[]
            a = a + Arco
            print('------------------------')
            print('     ',Arco)
            print('------------------------')
            with open(Arco,'r') as info:  #Lee el archivo json
                prueba = json.loads(info.read())
                for p in prueba:
                    ListaContar.append(p)
            print('Cantidad de registros dentro de archivo: ',len(ListaContar))                  
    else:
        print('Comando invalido')
    
def Reportar():
    l=""
    print('')
    print('---------------------')
    print('Archivos Cargados:') #Lista de archivos cargados
    for Listado in ArCorrectos:
            l = l + Listado + " "
            print(Listado)
    print('---------------------')
    print("""
    INSTRUCCIONES:
    Para poder ver la cantidad de registros dentro del archivo json debe escribir el comando REPORTAR
    seguido del numero de registros que desea agregar al reporte
    """)
    a=""
    reportar=input() #Ingresar lo que se desea sumar
    reportar=reportar.lower() #Case Insensitive
    rep=reportar.split()
    print(rep)
    repcero=rep[0]
    repcero=repcero.lower()
    n=int(rep[1])
    print (repcero)
    print (n)
    if repcero=='reportar':
        ListaReportados=[]
        for Arco in ArCorrectos: #Recorre la lista de correctos
            ListaReportar=[]
            a = a + Arco
            print('------------------------')
            print('     ',Arco)
            print('------------------------')
            with open(Arco,'r') as info:  #Lee el archivo json
                prueba = json.loads(info.read())
                for p in prueba:
                    ListaReportar.append(p)
            print(ListaReportar)
        i=0
        n=n-1
        while i <= n:
           print(ListaReportar[i]) #Recorre la lista hasta el valor de N ingresado
           ListaReportados.append(ListaReportar[i]) #Lo agrega a otra lista
           i+=1
        
        titulos=['Nombre','Edad','Activo','Promedio'] #Titulos de las filas
        doc = dominate.document(title='Registros') #Documento
        with doc.head:
            meta(charset="UTF-8")
            link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css", integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z", crossorigin="anonymous")
        with doc:
            with div(cls='Tabla', style="text-align: center"):
                h1('Reporte')
                with table(cls="table table-striped", style="text-align: center"):
                    for titulo in titulos:
                        with tr():
                            td(titulo)
                            x=0
                            while x <= len(ListaReportados)-1:
                                titulo=titulo.lower()
                                valor=str(ListaReportados[x].get(str(titulo)))
                                td(valor)
                                x+=1
        d=str(doc)
        f = open('reporte.html','wb')
        f.write(bytes(d,"ascii"))
        f.close()
        webbrowser.open_new_tab('reporte.html')
    else:
        print('Comando invalido')

                    





                
