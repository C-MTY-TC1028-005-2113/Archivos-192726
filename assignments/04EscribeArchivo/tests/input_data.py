# List of tuples
# Each tuple contains a test:
# - the first element are the inputs,
# - the second are the output,
# - and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    # Test case 1
    (
        ["3","Lupita","21","ITC","Lolita","19","ITC","Lalita","19","ITD"],
        ["Teclea cantidad de alumnos que quieras agregar:","name:","edad:","Carrera:","name:","edad:","Carrera:","name:","edad:","Carrera:"],
        "Revisa el modo al abrir el archivo, revisa si cerraste el archivo"
    ),
    (
        ["1","Chachis","21", "MC"],
        ["Teclea cantidad de alumnos que quieras agregar:","name:","edad:","Carrera:"],
        "Revisa el modo al abrir el archivo, revisa si cerraste el archivo"
    ),
    (
        ["2","Gerardo","21","ITC","Lorenzo","32","MES"],
        ["Teclea cantidad de alumnos que quieras agregar:","name:","edad:","Carrera:","name:","edad:","Carrera:"],
        "Revisa el modo al abrir el archivo, revisa si cerraste el archivo"
    )
    ]
