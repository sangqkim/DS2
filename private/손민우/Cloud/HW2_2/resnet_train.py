# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""ResNet Train/Eval module.
"""
import time
import six
import sys

import cifar10_download

cifar10_download.download()
import cifar_input
import numpy as np
import resnet_model
import tensorflow as tf
import parallax

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('train_data_path', '',
                           'Filepattern for training data.')
tf.app.flags.DEFINE_integer('image_size', 32, 'Image side length.')
tf.app.flags.DEFINE_string('ckpt_dir', None,
                           'Directory to keep the checkpoints. Should be a '
                           'parent directory of FLAGS.train_dir')
tf.app.flags.DEFINE_string('resource_info_file', 'resource_info',
                           'Resource information file')
tf.app.flags.DEFINE_string('run_option', 'HYBRID',
                           'Distributed training architecture')


def train(hps):
    """Training loop."""

    single_gpu_graph = tf.Graph()
    with single_gpu_graph.as_default():

        images, labels = cifar_input.build_input(
            'cifar10', FLAGS.train_data_path, hps.batch_size, 'train')
        model = resnet_model.ResNet(hps, images, labels, 'train')
        model.build_graph()

        truth = tf.argmax(model.labels, axis=1)
        predictions = tf.argmax(model.predictions, axis=1)
        precision = tf.reduce_mean(tf.to_float(tf.equal(predictions, truth)))

        ########################################################################
        #### FIXME: Get session for distributed environments using Parallax ####
        #### Pass parallax_config as an argument                            ####
        ########################################################################
        parallax_sess, num_workers, worker_id, num_replicas_per_worker = \
            parallax.parallel_run(single_gpu_graph,
                                  FLAGS.resource_info_file,
                                  parallax_config=parallax_config.build_config())

    for i in range(350000):

        _, global_step, cost, precision_ = \
            parallax_sess.run([model.train_op, model.global_step, model.cost, precision])

        if i % 100 == 0:
            print('step: %d, loss: %.3f, precision: %.3f' % (global_step[0], cost[0], precision_[0]))

            # Tuning learning rate
            train_step = global_step[0]
            if train_step < 10000:
                lrn_rate = 0.1
            elif train_step < 15000:
                lrn_rate = 0.01
            elif train_step < 20000:
                lrn_rate = 0.001
            else:
                lrn_rate = 0.0001
            feed_dict = {model.lrn_rate: []}
            for worker in range(num_replicas_per_worker):
                feed_dict[model.lrn_rate].append(lrn_rate)
            parallax_sess.run(model.global_step, feed_dict=feed_dict)


def main(_):
    batch_size = 128

    hps = resnet_model.HParams(batch_size=batch_size,
                               num_classes=10,
                               min_lrn_rate=0.0001,
                               lrn_rate=0.1,
                               num_residual_units=5,
                               use_bottleneck=False,
                               weight_decay_rate=0.0002,
                               relu_leakiness=0.1)

    train(hps)


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run()
