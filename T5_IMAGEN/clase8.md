# Segmentación y Superposición

## 1. Preparar las imágenes

Escenario y Gato

## 2. SEGMENGTACIÓN: Obtener un elemento de una imagen y quitar el fondo. 

#### Empecemos preparando el código

``` python

from PIL import Image
filename_cat = "gato.jpg"

with Image.open(filename_cat) as img_cat:
    img_cat.load()
    img_cat = img_cat.crop((800, 0, 1650, 1281))
    img_cat.show()
```
1. Comenta qué realiza este código

#### Segmentación
Las imágenes están compuestas por pixels de RGB, la segmentación a partir de cierto valor de umbral hacemos
que cada pixel pase a un mínimo y un máximo.

Pasamos la imagen a grey y utilizamos una función lambda en python que recorre cada pixel y pregunta si está dentro de un umbral de color

Pega este código dentro del with de la imagen...
```python
img_cat_gray = img_cat.convert("L")
img_cat_gray.show()
threshold = 100
img_cat_threshold = img_cat_gray.point(lambda x: 255 if x > threshold else 0)
img_cat_threshold.show()
```

Una vez que hemos segmentado obtenemos los colores de cada canal R G B

```python
red, green, blue = img_cat.split()
red.show()
green.show()
blue.show()
```

**Eje:** ¿Qué observas de cada canal? ¿Qué canal tiene mayor contraste?

Seleccionamos el canal con mayor contraste para realizar otra segmentación para ya quedarnos con la figura del gatuno

```
threshold = 57
img_cat_threshold = blue.point(lambda x: 255 if x > threshold else 0)
img_cat_threshold = img_cat_threshold.convert("1")
img_cat_threshold.show()
```

## CREACIÓN DE FILTROS MÁS SELECTIVOS
Prueba 1. Crea otro python llamado clase8_2.py

*Nota: Explicar los bucles en python*

```python

from PIL import ImageFilter
filename = "dot_and_hole.jpg"

with Image.open(filename) as img:
  img.load()
  for _ in range(3):
    img = img.filter(ImageFilter.MinFilter(3))
img.show()

```

**Eje** ¿Qué observas en la imagen?

``` python

img = img.filter(ImageFilter.MaxFilter(3))

```

Prueba 2. 

Realiza esta prueba realizando más pasadas con el bucle de los filtro en vez de 3 pasar a 10 y observa qué ocurre



```python

with Image.open(filename) as img:
  img.load()

  for _ in range(10):
    img = img.filter(ImageFilter.MinFilter(3))
  img.show()

  for _ in range(10):
    img = img.filter(ImageFilter.MaxFilter(3))

  img.show()

```

¿Qué observas? ¿Qué ocurre cuando iteras 10 veces?

### Añade estas dos funciones al primer python para utilizarlas con el Michi

*Nota: Explicar los métodos en python*

```python

def erode(cycles, image):
  for _ in range(cycles):
    image = image.filter(ImageFilter.MinFilter(3))
  return image


def dilate(cycles, image):
  for _ in range(cycles):
    image = image.filter(ImageFilter.MaxFilter(3))
  return image

```

## OBTENCIÓN DE LA MÁSCARA PARA EXTRAER LA FIGURA DE LA IMAGEN

**Nota:.** Hay que utilizar las funciones del apartado anterior Recuerda!!

Este proceso es un poco prueba y error hasta dar con el número de veces que tienes que ejecutar la erosión de la figura para
dejar una máscara decente

Añade esto al primer python python8_1.py

``` python

step_1 = erode(12, img_cat_threshold)
step_1.show()

```

Prueba esto...

```python

step_2 = dilate(58, step_1)
step_2.show()


