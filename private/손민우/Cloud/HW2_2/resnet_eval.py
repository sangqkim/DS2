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

import cifar_input
import numpy as np
import resnet_model
import tensorflow as tf

FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string('eval_data_path', '',
                           'Filepattern for eval data')
tf.app.flags.DEFINE_integer('eval_batch_count', 100,
                            'Number of batches to eval.')
tf.app.flags.DEFINE_string('eval_dir', '',
                           'Directory to keep eval outputs.')
tf.app.flags.DEFINE_string('ckpt_dir', '',
                           'Directory to keep the checkpoints. Should be a '
                           'parent directory of FLAGS.train_dir/eval_dir.')

def evaluate(hps):
  """Eval loop."""
  images, labels = cifar_input.build_input(
      'cifar10', FLAGS.eval_data_path, hps.batch_size, 'eval')
  model = resnet_model.ResNet(hps, images, labels, 'eval')
  model.build_graph()

  sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
  
  saver = tf.train.Saver() 
  
  ##################################
  ## FIXME: Make a summary writer ##
  ##################################
  summary_writer=tf.summary.FileWriter(FLAGS.eval_dir)

  try:
    ckpt_state = tf.train.get_checkpoint_state(FLAGS.ckpt_dir)
  except tf.errors.OutOfRangeError as e:
    tf.logging.error('Cannot restore checkpoint: %s', e)
  if not (ckpt_state):
    tf.logging.info('No model to eval yet at %s', FLAGS.ckpt_dir)
 
  best_precision = 0.
  for i in range(len(ckpt_state.all_model_checkpoint_paths)):
    tf.logging.info('Loading checkpoint %s', ckpt_state.all_model_checkpoint_paths[i])
    saver.restore(sess, ckpt_state.all_model_checkpoint_paths[i])
    total_prediction, correct_prediction = 0, 0

    for _ in six.moves.range(FLAGS.eval_batch_count):
      (summaries, loss, predictions, truth, train_step) = sess.run(
          [model.summaries, model.cost, model.predictions,
           model.labels, model.global_step])

      truth = np.argmax(truth, axis=1)
      predictions = np.argmax(predictions, axis=1)
      correct_prediction += np.sum(truth == predictions)
      total_prediction += predictions.shape[0]

    precision = 1.0 * correct_prediction / total_prediction
    best_precision = max(precision, best_precision)
    

    ########################################################
    ## FIXME: Add summary of precision and best precision ##
    ########################################################
    summ_precision = tf.Summary()
    summ_precision.value.add(tag='precision', simple_value=precision)
    summary_writer.add_summary(summ_precision, train_step)

    summ_best_precision = tf.Summary()
    summ_best_precision.value.add(tag='best_precision', simple_value=best_precision)
    summary_writer.add_summary(summ_best_precision, train_step)

    tf.logging.info('loss: %.3f, precision: %.3f, best precision: %.3f' %
                    (loss, precision, best_precision))
    summary_writer.flush()


def main(_):

  hps = resnet_model.HParams(batch_size=100,
                             num_classes=10,
                             min_lrn_rate=0.0001,
                             lrn_rate=0.1,
                             num_residual_units=5,
                             use_bottleneck=False,
                             weight_decay_rate=0.0002,
                             relu_leakiness=0.1)

  evaluate(hps)


if __name__ == '__main__':
  tf.logging.set_verbosity(tf.logging.INFO)
  tf.app.run()
