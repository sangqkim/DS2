from keras import models, layers, optimizers, regularizers
from keras import callbacks
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
# from keras.layers.advanced_activations import LeakyReLU

import os
import numpy as np
import pandas as pd
import seaborn as sns
import cv2
import matplotlib.pyplot as plt

from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.utils import shuffle
from random import randint
from tqdm import tqdm_notebook as tqdm
import gc
import glob # 유닉스 스타일 경로명 패턴 확장
import shutil # 셸 유틸리티: 파일 및 디렉터리 작업을 수행하는 데 사용
import warnings
from keras.applications.resnet import resnet
from keras.applications.resnet50 import ResNet50
from keras.applications import ResNet152V2
from keras.applications import inception_resnet_v2
from keras.applications import VGG19

import nni

def get_classlabel(class_code):
    labels = {2: 'glacier', 4: 'sea', 0: 'buildings', 1: 'forest', 5: 'street', 3: 'mountain'}

    return labels[class_code]


def get_images():
    # read train, test images
    # make it imbalance
    # then merge, shuffle, split

    dir_train = './data/seg_train'
    dir_test = './data/seg_test'

    label_str_to_int = {
        'buildings': 0,
        'forest': 1,
        'glacier': 2,
        'mountain': 3,
        'sea': 4,
        'street': 5,
    }

    train_images = []
    train_labels = []
    test_images = []
    test_labels = []

    # read train images
    for label_str in tqdm(os.listdir(dir_train), desc='dir', leave=False):
        label_int = label_str_to_int[label_str]
        image_dir = os.path.join(dir_train, label_str)

        if label_str == 'mountain':
            for _ in range(1):  # duplicate the mountain images n times
                for image_file in tqdm(os.listdir(image_dir), desc='images', leave=False):
                    image = cv2.imread(os.path.join(image_dir, image_file))  # Read image.
                    image = cv2.resize(image, (150, 150))  # Resize images. Some images are different sizes.
                    train_images.append(image)
                    train_labels.append(label_int)
        else:
            for image_file in tqdm(os.listdir(image_dir), desc='images', leave=False):
                image = cv2.imread(os.path.join(image_dir, image_file))  # Read image.
                image = cv2.resize(image, (150, 150))  # Resize images. Some images are different sizes.
                train_images.append(image)
                train_labels.append(label_int)

    # read test images
    for label_str in tqdm(os.listdir(dir_test), desc='dir', leave=False):
        label_int = label_str_to_int[label_str]
        image_dir = os.path.join(dir_test, label_str)

        for image_file in tqdm(os.listdir(image_dir), desc='images', leave=False):
            image = cv2.imread(os.path.join(image_dir, image_file))  # Read image.
            image = cv2.resize(image, (150, 150))  # Resize images. Some images are different sizes.
            test_images.append(image)
            test_labels.append(label_int)

    # treat imbalanced data

    x_train, y_train = shuffle(train_images, train_labels)
    x_test, y_test = shuffle(test_images, test_labels)

    return np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

class EpochCallback(callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        val_accuracy = logs["val_accuracy"]
        nni.report_intermediate_result(val_accuracy)  # report validation accuracy at each epoch


def get_model():
    res_conv = ResNet50(include_top=False,
                        weights='imagenet',
                        input_tensor=None,
                        input_shape=(150, 150, 3),
                        pooling=None, classes=1000)
    model = models.Sequential()
    model.add(res_conv)
    model.add(layers.Flatten())
    model.add(layers.Dense(1024, activation='relu'))
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(6, activation='softmax'))

    return model
def get_optimizer(hp_dict):
    lr = hp_dict["lr"]
    optimizer_name = hp_dict["optimizer_name"]
    if optimizer_name == "SGD":
        return optimizers.SGD(lr)
    if optimizer_name == "RMSprop":
        return optimizers.RMSprop(lr)
    if optimizer_name == "Adam":
        return optimizers.Adam(lr)
    raise NotImplementedError

os.makedirs("checkpoints", exist_ok=True)
experiment_id = nni.get_experiment_id()
trial_id = nni.get_trial_id()
model_path = f"checkpoints/{experiment_id}-{trial_id}.h5"

def tunable_train(hp_dict):
    x_train, y_train, x_test, y_test = get_images()
    model = get_model()
    optimizer = get_optimizer(hp_dict)

    alert_callback = EpochCallback()
    checkpoint_callback = callbacks.ModelCheckpoint(filepath=model_path, monitor='val_accuracy', verbose=1,
                                                    save_best_only=True)
    model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['acc'])
    model.fit(x_train, y_train, epochs=20, batch_size=hp_dict["batch_size"], validation_data=(x_test, y_test),
              callbacks=[alert_callback, checkpoint_callback])

    test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2, batch_size=512)

    return test_loss, test_acc
if __name__ == '__main__':
    hp_dict = nni.get_next_parameter()
    _, test_acc = tunable_train(hp_dict)
    nni.report_final_result(test_acc)  # report final accuracy



