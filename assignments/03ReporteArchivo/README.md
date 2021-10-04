![Tec de Monterrey](../../images/logotecmty.png)
# Reporte Archivos
Archivos-Reporte Archivos

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Agrega el código necesario para que tu programa lea un archivo de texto que se llama "Alumnos.txt" que contiene el siguiente contenido:
````
Lupita,21,ITC
Lolita,3,LAE
Marita,12,ITD
Popeye,30,IMD
Gladys,14,ITD
Juvia,18,ITC
Graciela,20,IMD
Silvia,22,LAE
Luis,23,LAE
Ramón,22,LAE
````

Separa el nombre, el número, y la carrera, y despliega en pantalla cuantos registros hay de cada carrera.

Salida:
```
ITC 2
LAE 4
ITD 2
IMD 2
```


**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
