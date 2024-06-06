# IA-20120140
img = cv.imread('D:/tec/9no Semestre/IA/Mover imagen
Este código leerá la imagen original, creará una versión redimensionada de ella en un área específica de una imagen en blanco y mostrará tanto la imagen original como la transformada.

19-02-2024.ipynb
invertirá los colores de la imagen y mostrará tanto la versión original como la invertida.
mostrará la imagen original y la imagen en blanco que contiene la imagen original en la esquina superior izquierda.
tomará cada píxel de la imagen original y lo colocará en un bloque de 3x3 en la nueva imagen, efectivamente escalando la imagen original.
moverá la imagen original reducida a la mitad hacia abajo y hacia la derecha por 100 píxeles, asegurando que los nuevos píxeles se coloquen dentro de los límites de la nueva imagen.
separa una imagen en color en sus componentes de color rojo, verde y azul, y muestra cada uno de ellos en una imagen color que destaca ese canal específico.
tomará la imagen original, separará los canales de color y luego combinará esos canales en diferentes órdenes para crear nuevas imágenes con canales intercambiados. Las nuevas imágenes se mostrarán en ventanas separadas.
permite visualizar las áreas de la imagen que corresponden a los colores especificados en los rangos HSV. Las ventanas mostrarán la imagen original, la imagen en espacio HSV, las máscaras individuales y combinadas, y la imagen resultante filtrada por la máscara combinada.

26-02-2024
Este código permitirá la detección en tiempo real de rostros usando la cámara del sistema y mostrará los resultados en una ventana.

Ejemplo
cargar y visualizar una imagen utilizando OpenCV.

Escalar imagen
escala una imagen en escala de grises al triplicar su tamaño en ambas dimensiones

caras
captura imágenes desde la cámara en tiempo real, detecta rostros en ellas y guarda recortes de los rostros en una carpeta correspondiente a una emoción específica.
carga imágenes de rostros previamente recortadas de diferentes carpetas, donde cada carpeta representa una emoción. Luego, utiliza estas imágenes para entrenar un clasificador de reconocimiento facial utilizando el método Local Binary Patterns Histograms (LBPH).
carga un modelo previamente entrenado para reconocimiento facial y lo utiliza para detectar emociones en tiempo real a partir de los rostros detectados en un flujo de video de la cámara.

Demo1
Muestra la implementación del juego con 3 balas

Incendios
Captura imágenes de un video cuadro por cuadro

Demo1pelota
Juego en el que el jugador debe esquivar la pelota, pelota que se mueve de forma aleatoria por todo el cuadro
