# clase 1 INTRODUCCIÓN A IMÁGENES EN PYTHON

```python

from PIL import Image

# imagen = Image.open ('./descarga.jpg')
# imagen.show()

with Image.open('./descarga2.jpg') as imagen2:
    imagen2.show()
    
    rgb2xyz = (
    0.412453, 0.357580, 0.180423, 0,
    0.212671, 0.715160, 0.072169, 0,
    0.019334, 0.119193, 0.950227, 0)

    out = imagen2.convert("RGB", rgb2xyz)
    out.show()
```
# TIPOS DE IMÁGENES
con Pillow son los de uso más extendido (BMP, EPS, GIF, IM, JPEG, MSP, PCX, PNG, TIFF, PPM, WebP, ICO, PSD, PDF, etc). Los tipos de imágenes dependen sobre todo del número de bits que se utilizan para representar la unidad de información de una imagen o píxel.

Clave	Tipo de imagen
1	1-bit por pixel, blanco y negro, almacena 1 pixel/byte
L	8-bit por píxel, blanco y negro
P	8-bit por píxel, asignada a cualquier otro modo usando una paleta de colores
RGB	3x8-bit por píxel, color verdadero
RGBA	4x8-bit por píxel, color verdadero con true color con máscara de transparencia
CMYK	4x8-bit por píxel, separación de colores
YCbCr	3x8-bit por píxel, formato de vídeo en color
LAB	3x8-bit por píxel, the L*a*b color space
HSV	3x8-bit por píxel, Hue, Saturation, Value color space)
I	32-bit signed integer pixels
F	32-bit floating point pixels
