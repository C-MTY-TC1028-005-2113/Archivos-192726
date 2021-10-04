import os.path

def elinina_prim_ult_pal_str(linea):
    primEsp = linea.find(" ")
    ultEsp = linea.rfind(" ")
    nuevaLinea = linea[primEsp + 1 : ultEsp]
    
    return nuevaLinea

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/01EliminaUltPrimPalabra/src/"
    with open(os.path.join(folder,"Data.txt")) as archEnt :
        with open(os.path.join(folder,"nuevasFrases.txt"), "w") as archSal :
            while True :
                linea = archEnt.readline()
                if linea != '':
                    lineaNueva = elinina_prim_ult_pal_str(linea)
                else :
                    break
            
                archSal.write(lineaNueva + "\n")


if __name__=='__main__':
    main()
