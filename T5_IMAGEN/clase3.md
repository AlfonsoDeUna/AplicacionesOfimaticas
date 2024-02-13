# ROTAR Y PEGAR IMÁGENES 

## Recortar imágenes

```python
from PIL import Image

# Abrir la imagen "pantera.jpg"
imagen = Image.open("pantera.jpg")

# Definir tupla con las coordenadas de la región
caja = (200, 100, 400, 300)

# Obtener región 
region = imagen.crop(caja)
region.show()
```

## ROTAR Y MOVER IMÁGENES

```python
# Girar región 90º
region = region.transpose(Image.ROTATE_90)
```

#### prueba los siguiente tipos de parámetros en transpose

* Image.FLIP_LEFT_RIGHT: 
* Image.FLIP_TOP_BOTTOM: 
* Image.ROTATE_90: 
* Image.ROTATE_180:
* Image.ROTATE_270: 
* Image.TRANSPOSE: 
* Image.TRANSVERSE:

## Pegar la imágen dentro de ella misma con una modificación

```python
# Pegar región girada en la imagen original
imagen.paste(region, caja)
```

## Mostrar imagen final y guardar

```python
imagen.show()
imagen.save("regiongirada90.jpg")
```
---

# JUNTAR DOS IMÁGENES PARA COMPARAR

PROGRAMA COMPLETO, CREA UN NUEVO FICHERO PYTHON EN VISUAL STUDIO CODE Y PREUBA EL SIGUIENTE CÓDIGO.

```python
from PIL import Image
final = Image.new("RGB",(1000,600),"black")
imagen1 = Image.open("OMAHA1.jpg")
imagen2 = Image.open("OMAHA2.jpg")
final.paste(imagen1, (0,0))
final.paste(imagen2, (600,0))
final.show()
```

# EJERCICIOS

## EJERCICIO1: CREA DOS IMÁGENES NUEVAS A PARTIR DE UNA. TIENE QUE MODIFICAR PARTES DE LA IMAGEN Y COMPONER DOS NUEVAS UTILIZANDO TRANSPOSE

## EJERCICIO 2: CREA UNA IMAGEN NUEVA A TRAVÉS DE PEGAR 2 Ó MÁS IMÁGENES EN MODO BANNER PARA PODER UTILIZARLO EN UN BANNER PARA UNA PÁGINA WEB



#
