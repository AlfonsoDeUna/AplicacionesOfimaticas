# COMPARAR IMÁGENES

```python

from PIL import Image, ImageChops

imagen1 = Image.open('./OMAHA1.jpg')
imagen2 = Image.open('./OMAHA2.jpg')
#imagen1.show()
#imagen2.show()
imagen1.resize((400,400))
imagen2.resize((400,400))


diff = ImageChops.difference(imagen2,imagen1)
diff2 = ImageChops.difference(imagen1,imagen2)

#threshold = 30
#diff = diff.point(lambda x: 0 if x < threshold else 255)

diff2.show()
diff.show()
```

## EJERCICIO 1: COMPARA DOS IMÁGENES CON ESTE MÉTODO. LA MEJOR IMAGEN GANA

