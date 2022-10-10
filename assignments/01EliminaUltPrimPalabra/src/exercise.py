import os.path

def elimina_primera_ultima_palabra_str(linea):
    if linea.count(" ") >= 2:
        pos = linea.index( " ")
        pos2 = linea.rindex(" ")
        extrae = linea[pos + 1:pos2]
        print(extrae)

    return extrae

def main():
    #escribe tu código abajo de esta línea
    folder = "assignments/01EliminaUltPrimPalabra/src/"
    with open(os.path.join(folder,"Data.txt")) as archEnt :
        with open(os.path.join(folder,"nuevasFrases.txt"), "w") as archSal :
            for linea in archEnt:
                archSal.write(elimina_primera_ultima_palabra_str(linea) )


if __name__=='__main__':
    main()
