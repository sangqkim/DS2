import numpy as np
import sys, json, os

import tensorflow as tf

NUM_DATA=1152
def input(batch_size):
  x_train = tf.data.Dataset.from_tensor_slices(tf.random.uniform([NUM_DATA, 20]))
  y_train = tf.data.Dataset.from_tensor_slices(tf.random.uniform([NUM_DATA,1], minval=0, maxval=1, dtype=tf.dtypes.int32))
  train_dataset = tf.data.Dataset.zip((x_train, y_train)).batch(batch_size).repeat()
  return train_dataset

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, input_dim=20, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
BATCH_SIZE=128
train_dataset = input(BATCH_SIZE)
model.fit(x=train_dataset, epochs=3, steps_per_epoch=NUM_DATA/BATCH_SIZE)
