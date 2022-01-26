#HARE KRSNA
print('Hare Krsna')
import datetime
import os

from django.core.files.storage import default_storage
from django.conf import  settings
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub


print(datetime.datetime.now())

if __name__ != '__main__':
    def breed(request):
        for file in os.listdir('media'):
            if 'rk'in file:
                os.remove((os.path.join('media', file)))
        file = default_storage.save('rk.jpg', request.FILES['SentFile'])
        print(datetime.datetime.now())
        
        image = tf.io.read_file('./media/rk.jpg')
        image = tf.image.decode_image(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.expand_dims( tf.image.resize(image, size=[224,224]), axis=0)

        model_path = os.path.join(settings.MODELS, 'dog_breeds_mobilenetv2_Adam_v1_.h5')
        apc = os.path.join(settings.MODELS, 'jps.txt')

        with open (apc, 'r') as f:
            breeds_name = np.array(f.read().split(sep=','))
        model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})

        prediction = model.predict(image)
        pred_breed = breeds_name[np.argmax(prediction)]
        pred_breed = pred_breed.replace("'",'')
        print(datetime.datetime.now())

        return pred_breed


def fruits(request):
    for file in os.listdir('media'):
        if 'gn' in file:
            os.remove(os.path.join('media', file))

    file = default_storage.save('gn.jpg', request.FILES['SentFile'])
    model_path = os.path.join(settings.MODELS, 'mobilenet_v2_130_224.h5')

    model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer})

    jps = os.path.join(settings.MODELS, 'apc.txt')
    with open(jps, 'r') as f:
        classes = np.array(f.read().split(sep=','))

    image = tf.keras.utils.load_img('./media/gn.jpg',target_size=(224,224))
    image_array = tf.keras.utils.img_to_array(image)
    image_ex = tf.expand_dims(image_array, 0)

    pred = model.predict(image_ex)
    pred_class = classes[np.argmax(pred)]

    return pred_class