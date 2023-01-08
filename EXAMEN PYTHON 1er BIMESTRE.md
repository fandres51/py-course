# 1) Examen

## 2) Crear un vector de ceros de tamaño 10

## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.

## 5) Crear una matriz de 3 x 3 con valores del cero al 8

## 6) Encontrar los indices que no sean cero en un arreglo

```python
import numpy as np
arreglo = [1,2,0,0,4,0]
```

## 7) Crear una matriz de identidad 3 x 3 

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos

## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor

## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)

## 11) ¿Como crear una serie de una lista, diccionario o arreglo?

```python
import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
```

## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

```python
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict) 
# Transformar la serie en dataframe y hacer una columna indice
```

## 13) ¿Como combinar varias series para hacer un DataFrame?

```python
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
```

## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?

```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
```

## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?

```python
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
```

## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?

```python
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
```

## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?

```python
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
```

## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?


```python
ser = pd.Series(np.random.randint(1, 10, 35))
shape(7,5)
```

## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?


```python
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
```

## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?


```python
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
```


## 21)¿Obtener la media de una serie agrupada por otra serie?

`groupby` tambien esta disponible en series.


```python
frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

```


## 22)¿Como importar solo columnas especificas de un archivo csv?

https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.





