# JUGAR CON LOS COLORES

---
## Colores
```python

img = Image.new('RGB',(200,200),(255,0,0))
img.show()
```
## RGB Todos los colores los puede definir con Rojo, verde y azul

```python
# using getrgb for yellow
img1 = ImageColor.getrgb("yellow")
print(img1)
 
# using getrgb for red
img2 = ImageColor.getrgb("red")
print(img2)
``` 

## convertir a gris
```python

filename = "imagen.jpg"
with Image.open(filename) as img:
    img.load()


cmyk_img = img.convert("CMYK")
gray_img = img.convert("L")  # Grayscale

```
---
# Ejercicio 1: convierte 3 imágenes de color a gris y únelas en una sola imagen.

**unir** lo vimos en una clase anterior como unir dos imágenes en una nueva.
---

Muestra su contenido

## Analizar los colores de una imagen

```python

red, green, blue = img.split()

```

## Crear una imagen en R G B

```python

zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

```

## Convertir píxeles de un color a otro color Ej. de blanco a amarillo

```python
img = Image.open("flower.jpg")
img = img.convert("RGB")
 
d = img.getdata()
 
new_image = []
for item in d:
 
    # change all white (also shades of whites)
    # pixels to yellow
    if item[0] in list(range(200, 256)):
        new_image.append((255, 224, 100))
    else:
        new_image.append(item)
 
# update image data
img.putdata(new_image)
 
# save new image
img.save("flower_image_altered.jpg")
```
---
# Ejercicio: Cambia colores de 3 imágenes. Busca que color quieres modificar y cambialo por otro
---

## Crear texto dentro de imágenes

#### Ejemplo 1
```python

    image = Image.new("RGB", (200, 200), "green")
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), "Hello from")
    draw.text((10, 25), "Pillow",)
```


#### Ejemplo 2

Fuente: https://github.com/larsenwork/Gidole

```python

    image = Image.open(input_image_path)
    draw = ImageDraw.Draw(image)
    y = 10
    for font_size in range(12, 75, 10):
        font = ImageFont.truetype("Gidole-Regular.ttf", size=font_size)
        draw.text((10, y), f"Chihuly Exhibit ({font_size=}", font=font)
        y += 35
```

---
# Ejercicio: Añade texto a imágenes en plan titulares de prensa
---

## Crear rectángulos

```python
image = Image.new("RGB", (400, 400), "blue")
    draw = ImageDraw.Draw(image)
    draw.rectangle((200, 100, 300, 200), fill="red")
    draw.rectangle((50, 50, 150, 150), fill="green", outline="yellow",
                   width=3)
```

### Elipses

```python
draw.ellipse((100, 100, 150, 200), fill=(255, 0, 0), outline=(0, 0, 0))
```

## Crear líneas dentro de una imagen

```python

def line(image_path, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange"]

    for i in range(0, 100, 20):
        draw.line((i, 0) + image.size, width=5, fill=random.choice(colors))

    image.save(output_path)
```
---
# Ejercicio: Cree una imagen compuesta de dibujos
---
---
# Ejercicio: Añade formas a dibujos
---
