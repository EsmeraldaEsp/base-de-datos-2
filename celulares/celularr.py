'''#Importar la librería sqlite3 para trabajar con bases de datos SQLite.
import sqlite3
##Conectarse (o crear) una base de datos llamada “celulares.db”.
def crear_base_datos():
    conn=sqlite3.connect("celulares.db")
    cursor=conn.cursor() 
    cursor.execute("""CREATE TABLE IF NOT EXISTS celulares(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    precio REAL INTEGER NOT NULL)
                    
                    """)
    conn.commit()
##Crear un cursor para ejecutar sentencias SQL.
def registrar_celulares(marca, modelo, precio):
    conn=sqlite3.connect("celulares.db")
    cursor=conn.cursor()
    cursor.execute('''
                    INSERT INTO celulares (,marca,modelo,precio)
                   VALUES(?,?,?)''',(marca,modelo,precio))
    conn.commit()
##Crear la tabla “celulares” si no existe, con los campos:

##id (clave primaria autoincremental)


##modelo (texto)

##precio (número real)

##Definir la función agregar_celular() que:
def agregar_celular(marca,modelo,precio):
    conn=sqlite3.connect("celulares.db")
    cursor=conn.cursor()
    cursor.execute('''
                   ''' INSERT INTO celulares (marca,modelo,precio)
                   VALUES(?,?,?)''',(marca,modelo,precio))
    '''print("El celular se a registrado correctamente")
    conn.commit()
    conn.close()'''

##Pide al usuario ingresar la marca del celular.
'''def menu():
    while True:
        print("1.Agregar celular")
        opcion=input("Elige una opcion: ")

        if opcion=="1":
            marca= input("Ingresa la marca del celular: ")
##Pide al usuario ingresar el modelo del celular.
            modelo= input("Ingresa el modelo del celular:")
##Pide al usuario ingresar el precio del celular.
            precio= float(input("Ingesa el precio del celular:"))
##Inserta los datos en la tabla celulares.
            agregar_celular(marca,modelo,precio)
##Guarda los cambios en la base de datos.

##Muestra un mensaje de confirmación indicando que el celular fue agregado exitosamente.
###diego andas por aqui?
crear_base_datos()
menu()