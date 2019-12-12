import numpy as np
import sys, json, os

import tensorflow as tf

NUM_DATA=1152
def input(batch_size):
  x_train = tf.data.Dataset.from_tensor_slices(tf.random_uniform([NUM_DATA, 20]))
  y_train = tf.data.Dataset.from_tensor_slices(tf.cast(tf.random_uniform([NUM_DATA,1], minval=0, maxval=1, dtype=tf.int32), tf.float32))
  train_dataset = tf.data.Dataset.zip((x_train, y_train)).batch(batch_size).repeat()
  return train_dataset

single_gpu_graph = tf.Graph()
with single_gpu_graph.as_default():
  BATCH_SIZE=128
  train_dataset = input(BATCH_SIZE)
  iterator = train_dataset.make_initializable_iterator()
  inputs, labels = iterator.get_next()

  model = tf.keras.Sequential()
  model.add(tf.keras.layers.Dense(64, input_dim=20, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Dense(64, activation='relu'))
  model.add(tf.keras.layers.Dropout(0.5))
  model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

  logits = model(inputs, training=True)  
  accuracy = tf.metrics.accuracy(
        labels=labels, predictions=tf.argmax(logits, axis=1))[1]
  loss = tf.reduce_mean(tf.keras.backend.binary_crossentropy(labels, logits))
  step = tf.train.get_or_create_global_step()
  optimizer=tf.train.RMSPropOptimizer(1.0)
  train_op = optimizer.minimize(loss, step)
  
  init_op = tf.group(tf.initialize_all_variables(),
                     tf.initialize_local_variables())
   
sess = tf.Session(graph=single_gpu_graph)
sess.run(init_op)
sess.run(iterator.initializer)
NUM_EPOCHS = 3
for i in range(NUM_EPOCHS * NUM_DATA / BATCH_SIZE):
  step_, loss_, accuracy_, _ = sess.run([step, loss, accuracy, train_op])

  if i % 2 == 0:
    print('step:%d, loss: %2f, accuracy: %2f' % (step_, loss_, accuracy_))

