![Tec de Monterrey](../../images/logotecmty.png)
# Escribe Archivo
Archivos-Escribe Archivo

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Añade las instrucciones para añadir registros a un archivo llamado Alumnos.txt, el archivo debe tener el siguiente formato:
Lupita,21,ITC
Lolita,23,LAE
Marita,12,ITD
Popeye,30,IMD

el programa debe leer la cantidad de alumnos que quieres añadir al final del archivo, posteriormente debe
leer y grabar la información de cada uno de ellos en el archivo, ejecuta el programa.

La salida del programa debe de ser exactamente de la siguiente forma:

```
Caso 1:
Teclea cantidad de alumnos que quieras agregar:1
name:Chachis
edad:21
Carrera:MC

Caso 2:
Teclea cantidad de alumnos que quieras agregar:2
name:Gerardo
edad:21
Carrera:ITC
name:Lorenzo
edad:32
Carrera:MES
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
