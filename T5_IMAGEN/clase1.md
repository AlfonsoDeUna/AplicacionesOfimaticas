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
