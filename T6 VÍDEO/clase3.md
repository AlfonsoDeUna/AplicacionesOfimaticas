# COMO ESCRIBIR EN UN VIDEO USANDO OPENCV

Vamos a partir de un vídeo obtener otro donde le vamos añadir un recuadro.

## PASOS PARA REALIZAR LA PRÁCTICA DE HOY

### importar liberías

```python
import cv2
```

### abrir y leer un vídeo en el que vamos a escribir

```python
cap = cv2.VideoCapture("path")
```

### Crear un fichero de salida utilizando el método cv2.VideoWriter_fourcc()

```pytyhon
<VideoWriter object> = cv2.VideoWriter(filename, fourcc, fps, frameSize)
```
filename es el nombre que tendrá el archivo de video y la extensión 'video.avi'
fourcc es un código que utiliza 4 caracteres con que se identifica cada códec. Un códec es un dispositivo o programa informático que puede comprimir o descomprimir flujos y señales de datos digitales.
los códecs se utilizan para codificar y descodificar archivos de vídeo.
fps velocidad de fotogramas de la secuencia de video.
frameSize tamaño de los frames que componen el video

#### En nuestro caso

```python
output = cv2.VideoWriter(“path”,cv2.VideoWriter_fourcc(*’MPEG’),30,(1080,1920))
```

### Recorrer el vídeo leyendo frame a frame del vídeo
```python

while(True): 
        ret, frame = cap.read() 
        if(ret): 
              
            # añadir el rectángulo
            
              
            # Escribir el nuevo frame en el nuevo vídeo de salida 

            # opcional sirve para mostrar el vídeo en tiempo real.
            cv2.imshow("output", frame) 
            if cv2.waitKey(1) & 0xFF == ord('s'): 
                break
# liberar recursos (muy importante)!!
cv2.destroyAllWindows() 
output.release() 
cap.release() 
```

### Crear un rectángulo con OpenCV

cv2.rectangle(image, start_point, end_point, color, thickness)

image = es la imagen donde el rectángulo lo vamos a dibujar
start_point = coordenadas de comienzo de un rectángulo (x,y)
end_point = coordenadas del final del rectángulo (x,y)
color = RGB (255,0,0) por ejemplo sería azul
thickness = el tamaño del borde y si es -1px rellena el rectángulo del color seleccionado

```python
cv2.rectangle(frame, (100,100), (500,500), (0,255,0), 3)
```

### Añadir a un vídeo un frame

```python
output.write(frame)
```

## Ejercicios
1. Dibujar varios rectángulos de diferentes tamaños
2. Dibujar varios rectángulos de diferentes colores
3. Dibujar varios rectángulos con color para tapar partes del vídeo

## Otros tipos de formas

### Círculos
```python
cv2.circle(image, center_coordinates, radius, color, thickness)
```
`

