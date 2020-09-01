Universidad de San Carlos de Guatemala
Facultad de Ingeniería
Escuela Ciencias y Sistemas
Laboratorio Lenguajes Formales y de programacion A+
Luis Andrés de la Peña Pineda
201900450

# Bienvenido a SimpleQL

Introducción:

SimpleQl es un menu el cual te permite facilitar la busqueda, por medio de comandos, de los registros de un archivo de tipo JSON.

**El archivo JSON debe de estar en la misma carpeta que el .py**

### Menú: 

Al iniciar el programa se le presenta el siguiente menú en la consola:
<p align="center">
 SIMPLEQL    
 ------------------------
 Menu de inicio
 ------------------------
1. Cargar
2. Seleccionar
3. Maximo
4. Minimo
5. Suma
6. Cuenta
7. Reportar
8. Salir

Opcion elegida:
</p>

**En la parte de "Opcion elegida" se escribe el *NUMERO* de la opcion que desea.**
### Opciones:

***Todos los comandos no son afectados por como sean escritos (Mayusculas o minusculas)**

1. Cargar:
	Para cargar los archivos json con los cuales desea trabajar debe poner el comando     **Cargar** seguido de los archivos que desea cargar separados por coma:
    (Ejemplo: Cargar archivoN.json, archivoM.json).

2. Seleccionar:
	 Para poder elegir los atributos dentro de los archivos cargados debera escribir **SELECCIONAR**  seguido de los atributos separados por coma, luego la palabra **DONDE** seguido de la condicion.
    *(EJEMPLO: SELECCIONAR nombre, edad DONDE edad=10)*. Si desea ver todos los atributos de todos los registros el comando es SELECCIONAR * .

3. Maximo:
	Para poder ver el valor maximo de un atributo escriba la palabra **MAXIMO** seguida del  atributo los cuales solo pueden ser edad o promedio.
    (SOLO ATRIBUTOS NUMERICOS, EJEMPLO: Maximo edad).

4. Minimo:
	INSTRUCCIONES:
    Para poder ver el valor minimo de un atributo escriba la palabra **MINIMO** seguida del  atributo los cuales solo pueden ser edad o promedio.
    (SOLO ATRIBUTOS NUMERICOS, EJEMPLO: Minimo edad).

5. Suma:
	Para poder ver la suma de un atributo escriba la palabra **SUMA** seguida del atributo  los cuales solo pueden ser edad o promedio.
    (SOLO ATRIBUTOS NUMERICOS, EJEMPLO: Suma edad).

6. Cuenta:
	 Para poder ver la cantidad de registros dentro del archivo json debe escribir el comando **CONTAR**.

7. Reportar:
	Para poder ver la cantidad de registros dentro del archivo json debe escribir el comando **REPORTAR** seguido del numero de registros que desea agregar al reporte. El reporte sera presentado en un html en su navegador. (EJEMPLO: reportar 4).