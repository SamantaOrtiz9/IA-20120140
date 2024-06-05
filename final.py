import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.transform import resize
import matplotlib.image as mpimg
import tensorflow as tf


saved_model_path = r"D:\tec\9no Semestre\IA\Proyectos finales\CNN\model"


loaded = tf.saved_model.load(saved_model_path)
print(list(loaded.signatures.keys()))  


infer = loaded.signatures['serving_default']
print(infer.structured_outputs)  


desastres = ['asaltos', 'incendios', 'inundaciones', 'RoboCasaHabitacion', 'tornados']

def process_and_predict_image(filepath):
 image = mpimg.imread(filepath)
 image_resized = resize(image, (30, 30), anti_aliasing=True, clip=False, preserve_range=True)
 image_resized = np.expand_dims(image_resized, axis=0)  
 image_resized = image_resized.astype('float32') / 255.  


 input_tensor = tf.convert_to_tensor(image_resized)
 predictions = infer(input_tensor)
 output_tensor_name = list(predictions.keys())[0]  
 predicted_classes = predictions[output_tensor_name]  
 predicted_label = desastres[tf.argmax(predicted_classes, axis=1).numpy()[0]]

 return predicted_label, image

filenames = [r'D:\tec\9no Semestre\IA\Proyectos finales\CNN\imagen\9.png']

for filepath in filenames:
 prediction, image = process_and_predict_image(filepath)
 
 plt.imshow(image)
 plt.title(f'Prediction: {prediction}')
 plt.axis('off')
 plt.show()