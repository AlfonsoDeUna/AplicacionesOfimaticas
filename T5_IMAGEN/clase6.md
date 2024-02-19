# FILTROS:  Desenfocar, afinar y suavizar

Para aplicar con Pillow un filtro a una imagen se utiliza el módulo ImageFilter. 

Debemos tener en cuenta que, a veces, cuando se aplica un filtro los cambios a observar serán más o menos sutiles en función al tipo de imagen que procesemos.

## TIPOS DE FILTROS

* BLUR: Desenfocar una imagen
* CONTOUR: Marcar contornos
* DETAIL: Resaltar detalle
* EDGE_ENHANCE y EDGE_ENHANCE_MORE: Realzar bordes
* EMBOSS: Obtener relieve
* FIND_EDGES: Buscar límites
* SMOOTH y SMOOTH_MORE: Suavizar la imagen
* SHARPEN: Afinar
---
#### Ejercicio: REALIZA EJEMPLOS DE LOS SIGUIENTES FILTROS
---

### BLUR: Desenfocar una imagen

  ```python
    from PIL import Image, ImageFilter
    imagen = Image.open("imagen.jpg")
    desenfocada = imagen.filter(ImageFilter.BLUR)
    desenfocada.show()
    desenfocada.save("desenfocada.jpg")
  ```

   Prueba ahora con:
     * ImageFilter.BoxBlur() 
     * ImageFilter.GaussianBlur():
     
### CONTOUR: Marcar contornos

  ```python
    contorneada = imagen.filter(ImageFilter.CONTOUR)
    contorneada.show()
    contorneada.save("contorneada.jpg")
  ```

### DETAIL: Resaltar detalle

  ```python
    detallar = imagen.filter(ImageFilter.DETAIL)
    detallar.show()
    detallar.save("detallada.jpg")
  ```
### EDGE_ENHANCE y EDGE_ENHANCE_MORE: Realzar bordes

  ```python
    realzarbordes = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE)
    realzarbordes.show()
    realzarbordes.save("realzarbordes.jpg")
  ```
### EMBOSS: Obtener relieve

  ```python
    relieve = imagen.filter(ImageFilter.EMBOSS)
    relieve.show()
    relieve.save("relieve.jpg")
  ```
### FIND_EDGES: Buscar límites

  ```python
    limites = imagen.filter(ImageFilter.FIND_EDGES)
    limites.show()
    limites.save("limites.jpg")
  ```
### SMOOTH y SMOOTH_MORE: Suavizar la imagen

  ```python
    suavizar = imagen.filter(ImageFilter.SMOOTH_MORE)
    suavizar.show()
    suavizar.save("suavizar.jpg")
  ```
### SHARPEN: Afinar

  ```python
    afinar = imagen.filter(ImageFilter.SHARPEN)
    afinar.show()
    afinar.save("afinar.jpg")

  ```
---
## EJERCICIOS

1.  CREA UNA PÁGINA WEB A PARTIR DE UN DOCUMENTO DE TEXTO QUE TENGA LA EXTENSIÓN HTML

  La página web sirve de ejemplo de las imágenes con las que has experimentado
   
   ```html
      <html>
          <head></head>
          <body>
             <H1> FILTRO: SMOOTH (h1 es título en html) </H1>
              <P> Explica para que sirve el filtro (la etiqueta p es un párrafo en html) </p>
              <img src="ruta completa de la imagen "/>
          </body>
      </html>
  ```

2. compara la imagen con su filtro y pégalas una al lado de otra.
