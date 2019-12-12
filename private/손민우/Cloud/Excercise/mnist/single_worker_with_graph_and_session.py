# -*- coding: utf-8 -*-
"""multi_worker_with_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OM2xSxbsLXVoARXYI2orv75oA7RP9VkV

##### Copyright 2019 The TensorFlow Authors.
"""

#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## Overview

#This tutorial demonstrates multi-worker distributed training with Keras model using `tf.distribute.Strategy` API. With the help of the strategies specifically designed for multi-worker training, a Keras model that was designed to run on single-worker can seamlessly work on multiple workers with minimal code change.

#[Distributed Training in TensorFlow](../../guide/distributed_training.ipynb) guide is available for an overview of the distribution strategies TensorFlow supports for those interested in a deeper understanding of `tf.distribute.Strategy` APIs.

## Setup

# First, setup TensorFlow and the necessary imports.

"""## Preparing dataset

Now, let's prepare the MNIST dataset from [TensorFlow Datasets](https://www.tensorflow.org/datasets). The [MNIST dataset](http://yann.lecun.com/exdb/mnist/) comprises 60,000
training examples and 10,000 test examples of the handwritten digits 0–9,
formatted as 28x28-pixel monochrome images.
"""
import os
from mnist_model import * 

STEPS_PER_EPOCH = 60000 / BATCH_SIZE
NUM_EPOCHS=3

single_gpu_graph = tf.Graph()
with single_gpu_graph.as_default():
  train_datasets = make_datasets_unbatched().batch(BATCH_SIZE).repeat()
  iterator = train_datasets.make_one_shot_iterator()
  inputs, labels = iterator.get_next()
  single_worker_model = build_and_compile_cnn_model(forward_only=True)

  logits = single_worker_model(inputs, training=True)
  accuracy = tf.metrics.accuracy(
        labels=labels, predictions=tf.argmax(logits, axis=1))[1]
  loss = tf.keras.losses.sparse_categorical_crossentropy(labels, logits)
  optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001) 
  step = tf.train.get_or_create_global_step()
  train_op = optimizer.minimize(loss, step)
  loss = tf.reduce_mean(loss)

  init_op = tf.group(tf.initialize_all_variables(),
                     tf.initialize_local_variables())
  

sess = tf.Session(graph=single_gpu_graph)
sess.run(init_op)

# Create summary_writer for TensorBoard
summary_writer = tf.summary.FileWriter('tensorboard', single_gpu_graph)

for i in range(NUM_EPOCHS * STEPS_PER_EPOCH):
  step_, loss_, accuracy_, _ = sess.run([step, loss, accuracy, train_op])
  
  # Add loss value to the summary_writer
  loss_summ = tf.Summary()
  loss_summ.value.add(
        tag='Loss', simple_value=loss_)
  summary_writer.add_summary(loss_summ, step_)

  if i % 10 == 0:
    print('step:%d, loss: %2f, accuracy: %2f' % (step_, loss_, accuracy_))

