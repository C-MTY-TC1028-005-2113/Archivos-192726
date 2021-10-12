import os.path

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/02ArchivoCalculaPromedio/src/"
    with open(os.path.join(folder,"Data.txt")) as archEnt :
        with open(os.path.join(folder,"Resultados.txt"), "w") as archSal :
            pass



if __name__=='__main__':
    main()
