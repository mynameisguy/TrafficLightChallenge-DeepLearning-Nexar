import os

from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import keras.backend as K
from train import SqueezeNet
from consts import IMAGE_WIDTH, IMAGE_HEIGHT

TEST_FOLDER="./test"
K.set_image_dim_ordering('tf')

model = SqueezeNet(3, (IMAGE_HEIGHT, IMAGE_WIDTH, 3))
model.load_weights("trained_model/challenge1.weights")

with open('results.csv','w') as results:
    results.write("fname,class,p0,p1,p2\n")
    for root, dirnames, filenames in os.walk(TEST_FOLDER):
        for filename in filenames:
            filepath = os.path.join(root, filename)
            image = load_img(filepath, target_size=(224, 224))
            image = img_to_array(image)
            image /= 255.0
            image = np.expand_dims(image, axis=0)
            preds = model.predict(image)[0]
            line = filename + "," + str(np.argmax(preds))
            for i in range(3):
                line += "," + str(preds[i])

            results.write(line+'\n')

