import os.path

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/04EscribeArchivo/src/"
    with open(os.path.join(folder,"Alumnos.txt"), 'a') as archivo:
        # archivo = open("Alumnos.txt", 'a')
        #que operacion puedo hacer
        cantidad = int(input('Teclea cantidad de alumnos que quieras agregar:'))
        for K in range(cantidad):
            name = input('name:')
            edad = input('edad:')
            carrera = input('Carrera:')
          #Crear el registro del alumno - un string con \n para que salte de linea
            salida = name + ','+ edad + ','+ carrera + '\n'
          #Grabar el registro del alumno en el archivo f
            archivo.write(salida)


if __name__=='__main__':
    main()
