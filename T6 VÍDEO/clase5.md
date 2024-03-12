# PASAR UN VÍDEO A GRIS

Esta práctica es muy sencilla solo hay que buscar algunod de tus vídeos, por ejemplo, el de short de youtube que era una entrega que hay que realizar y adaptar este código para visualizar el vídeo en la escala de colores gris.



```python
 importing the module
import cv2 
# reading the video
source = cv2.VideoCapture('ruta del vídeo')
# running the loop
while True:
  
    # extracting the frames
    ret, img = source.read()
      
    # converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
    # displaying the video
    cv2.imshow("Live", gray)
  
    # exiting the loop
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
      
# closing the window
cv2.destroyAllWindows()
source.release()

```
