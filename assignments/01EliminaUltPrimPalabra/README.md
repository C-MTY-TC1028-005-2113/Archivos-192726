![Tec de Monterrey](../../images/logotecmty.png)
# Elimina Primera y Ultima Palabra
Archivos-Elimina Primera y Ultima Palabra


Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Añade una función que reciba una cadena de caracteres, y construya y regrese otra cadena que tenga la cadena original eliminando la primera y última palabra.

El programa debe tomar cada línea del archivo, llamar a la función, y luego colocar esa línea en un archivo de salida llamado "nuevasFrases.txt"

Entrada
Este programa toma la entrada del archivo Data.txt

Salida
Este programa genera la salida en un archivo llamado nuevasFrases.txt

<b>Ejemplo de archivo de entrada:</b>
```
Cuando cuentes cuentos,
cuenta cuantos cuentos cuentas,
porque si no cuentas cuantos cuentos cuentas
nunca sabrás cuantos cuentos cuentas tú
```

<b>Ejemplo de archivo de salida: </b>
```
cuentes
cuantos cuentos
si no cuentas cuantos cuentos
sabrás cuantos cuentos cuentas
```

**Nota:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
