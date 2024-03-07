# Añadir texto a un vídeo

## Añadir un texto a una imagen con OpenCV

La función putText puede añadir texto a una imagen o un frame de un vídeo

cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)

El color en RGB de (0,0,0) a (255,255,255)
ubicación es donde queremos que aparezca dentro de nuestra imagen el texto son dos coordenadas (x,y) que representan el recuadro del texto

#### Tipos de letra

* cv2.FONT_HERSHEY_SIMPLEX = 0
* cv2.FONT_HERSHEY_PLAIN = 1
* cv2.FONT_HERSHEY_DUPLEX = 2
* cv2.FONT_HERSHEY_COMPLEX = 3
* cv2.FONT_HERSHEY_TRIPLEX = 4
* cv2.FONT_HERSHEY_COMPLEX_SMALL = 5
* cv2.FONT_HERSHEY_SCRIPT_SIMPLEX = 6
* cv2.FONT_HERSHEY_SCRIPT_COMPLEX = 7
* cv2.FONT_ITALIC = 16

```python
#Importar librería cv2
import cv2
 
#Leer imagen
img = cv2.imread('la ruta de la imagen...')
 
#Características del texto
texto = "pone el texto que quieras"
ubicacion = (200,700)
font = cv2.FONT_HERSHEY_TRIPLEX
tamañoLetra = 25
colorLetra = (221,82,196)
grosorLetra = 10
 
#Escribir texto
cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
 
#Guardar imagen
cv2.imwrite('imagen_con_texto.jpg', img)
 
#Mostrar imagen
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Tipos de letra

* cv2.FONT_HERSHEY_SIMPLEX = 0
* cv2.FONT_HERSHEY_PLAIN = 1
* cv2.FONT_HERSHEY_DUPLEX = 2
* cv2.FONT_HERSHEY_COMPLEX = 3
* cv2.FONT_HERSHEY_TRIPLEX = 4
* cv2.FONT_HERSHEY_COMPLEX_SMALL = 5
* cv2.FONT_HERSHEY_SCRIPT_SIMPLEX = 6
* cv2.FONT_HERSHEY_SCRIPT_COMPLEX = 7
* cv2.FONT_ITALIC = 16

### Ejercicio añade todos los tipos de letra a una imagen

## Poner Texto a un vídeo con OPENCV

También podemos usar la función putText() añade texto a un frame de un vídeo vídeo


``` python
import cv2 
  
  
cap = cv2.VideoCapture('video_ejemplo.mp4') 
  
while(True): 
      
    # Capture frames in the video 
    ret, frame = cap.read() 
  
    # describe the type of font 
    # to be used. 
    font = cv2.FONT_HERSHEY_SIMPLEX 
  
    # Use putText() method for 
    # inserting text on video 
    cv2.putText(frame,  
                'TEXT ON VIDEO',  
                (50, 50),  
                font, 1,  
                (0, 255, 255),  
                2,  
                cv2.LINE_4) 
  
    # Display the resulting frame 
    cv2.imshow('video', frame) 
  
    # creating 'q' as the quit  
    # button for the video 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# release the cap object 
cap.release() 
# close all windows 
cv2.destroyAllWindows() 
```

