# Pegar imágenes con máscara

## ¿Cómo ajustar dos imágenes al mismo tamaño? Segunda manera

```python

from PIL import Image, ImageDraw, ImageFilter

im1 = Image.open('data/src/lena.jpg')
im2 = Image.open('data/src/rocket.jpg').resize(im1.size)

```
## Aplicar una máscara a dos imágenes

```python

mask = Image.new("L", im1.size, 128)
im = Image.composite(im1, im2, mask)
im = Image.blend(im1, im2, 0.5)
```
**blend()** es un método que crear composiciones aplicando un ratio o alpha (transparencia)
Podemos jugar con la transparencia que va del 0.0 al 1.0

## Crear máscaras

Ahora vamos a crear una composición utilizando una figura geométrica como puede ser un círculo o un rectángulo

```python
mask = Image.new("L", im1.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((140, 50, 260, 170), fill=255)
im = Image.composite(im1, im2, mask)
```

# Ejercicio 1 crea dos imágenes con otras figuras geométricas, investiga en Pillow como crear otras figuras y realiza composiciones con imágenes.

## Efectos en las máscaras

A partir del código de ejemplo anterior, vamos a crear un efecto de difuminado en la máscara
con **ImageFilter**

````python
mask_blur = mask.filter(ImageFilter.GaussianBlur(10))
im = Image.composite(im1, im2, mask_blur)
```

## Efecto de gradiente en máscaras

Primero vamos a generar gradientes R,G,B

### Creación de un gradiente

```python

from PIL import Image
import numpy as np

def get_gradient_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

    return result

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (True, True, True))
Image.fromarray(np.uint8(array)).save('data/dst/gray_gradient_h.jpg', quality=95)
```

Ahora prueba los siguientes gradientes:

```python

array = get_gradient_3d(512, 256, (0, 0, 0), (255, 255, 255), (False, False, False))
Image.fromarray(np.uint8(array)).save('data/dst/gray_gradient_v.jpg', quality=95)
```

otro gradiente

```
array = get_gradient_3d(512, 256, (0, 0, 192), (255, 255, 64), (True, False, False))
Image.fromarray(np.uint8(array)).save('data/dst/color_gradient.jpg', quality=95)
```
---
# Ejercicio crea varios gradientes en Grey 'L' y RGB
---

## Aplicar gradientes a una composición de imágenes

Es necesario crear un fichero de gradientes con el código en el apartado anterior

``` python

mask = Image.open('data/src/gradation_h.jpg').convert('L').resize(im1.size)
im = Image.composite(im1, im2, mask)

```
# PROYECTO DE ESTA TAREA:

## Crea 3 imágenes utilizando las técnicas vistas en clase
