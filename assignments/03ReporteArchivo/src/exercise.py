import os.path

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/03ReporteArchivo/src/"
    with open(os.path.join(folder,"Alumnos.txt")) as file:
        lista = file.readlines( )
        cantidad = [0] * 10
        lista_carrera = []
        for index, alumno in enumerate(lista):
            alumno = alumno[:-1]
            alumno = alumno.split(',')
            name, edad, carrera = alumno

            if carrera not in lista_carrera:
                lista_carrera.append(carrera)
                cantidad [lista_carrera.index(carrera)] += 1
            else:
                cantidad [lista_carrera.index(carrera)] += 1

            print(f'{index + 1:<3}{name:<10} {edad:<4} {carrera}')
        for carrera, can in zip(lista_carrera, cantidad):
            print(carrera, can)

if __name__=='__main__':
    main()
