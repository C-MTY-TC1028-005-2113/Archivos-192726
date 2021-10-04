import os.path

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/02ArchivoCalculaPromedio/src/"
    with open(os.path.join(folder,"Data.txt")) as archEnt :
        with open(os.path.join(folder,"Resultados.txt"), "w") as archSal :
            prom = 0
            cont = 0
            while True :
                linea = archEnt.readline()
                if linea != '':
                    num = linea.replace("\n","")
                    prom += int(num)
                    cont += 1
                else :
                    break
                
                
            
            archSal.write(str(round(prom/cont,2)))



if __name__=='__main__':
    main()
