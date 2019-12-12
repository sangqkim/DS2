#Copyright 2016 The TensorFlow Authors. All Rights Reserved.
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

"""CIFAR dataset input module.
"""

import tensorflow as tf
import parallax

def build_input(dataset, data_path, batch_size, mode):
  """Build CIFAR image and labels.

  Args:
    dataset: Either 'cifar10' or 'cifar100'.
    data_path: Filename for data.
    batch_size: Input batch size.
    mode: Either 'train' or 'eval'.
  Returns:
    images: Batches of images. [batch_size, image_size, image_size, 3]
    labels: Batches of labels. [batch_size, num_classes]
  Raises:
    ValueError: when the specified dataset is not supported.
  """
  image_size = 32
  if dataset == 'cifar10':
    label_bytes = 1
    label_offset = 0
    num_classes = 10
  elif dataset == 'cifar100':
    label_bytes = 1
    label_offset = 1
    num_classes = 100
  else:
    raise ValueError('Not supported dataset %s', dataset)

  depth = 3
  image_bytes = image_size * image_size * depth
  record_bytes = label_bytes + label_offset + image_bytes

  def parse_data(value): 
    # Convert these examples to dense labels and processed images.
    record = tf.reshape(tf.decode_raw(value, tf.uint8), [record_bytes])
    label = tf.cast(tf.slice(record, [label_offset], [label_bytes]), tf.int32)

    # Convert from string to [depth * height * width] to [depth, height, width].
    depth_major = tf.reshape(tf.slice(record, [label_offset + label_bytes], [image_bytes]),
                           [depth, image_size, image_size])
    # Convert from [depth, height, width] to [height, width, depth].
    image = tf.cast(tf.transpose(depth_major, [1, 2, 0]), tf.float32)

    if mode == 'train':
      image = tf.image.resize_image_with_crop_or_pad(
        image, image_size+4, image_size+4)
      image = tf.random_crop(image, [image_size, image_size, 3])
      image = tf.image.random_flip_left_right(image)
      # Brightness/saturation/constrast provides small gains .2%~.5% on cifar.
      # image = tf.image.random_brightness(image, max_delta=63. / 255.)
      # image = tf.image.random_saturation(image, lower=0.5, upper=1.5)
      # image = tf.image.random_contrast(image, lower=0.2, upper=1.8)
      image = tf.image.per_image_standardization(image)

    else:
      image = tf.image.resize_image_with_crop_or_pad(
        image, image_size, image_size)
      image = tf.image.per_image_standardization(image)

    return image, label

  ###################################################################################
  #### FIXME: Partition dataset so that each worker can read disjoint data files ####
  ###################################################################################
  data_files = tf.gfile.Glob(data_path)
  data_files.sort()
  ds = tf.data.Dataset.from_tensor_slices(data_files).repeat()
  ds = parallax.shard.shard(ds)
  ds = ds.apply(
        # Read and preprocess cycle_length files concurrently
        tf.contrib.data.parallel_interleave(
            lambda filename: tf.data.FixedLengthRecordDataset(filename, record_bytes),
            cycle_length=len(data_files)))

  # Prefetch BATCH_SIZE items
  ds = ds.prefetch(batch_size)

  ds = ds.shuffle(50000)
  ds = ds.repeat()

  ds = ds.map(parse_data, num_parallel_calls=batch_size)
  ds = ds.batch(batch_size)
  ds = ds.prefetch(1)
 
  iterator = ds.make_one_shot_iterator()
  images, labels = iterator.get_next()
  

  images = tf.reshape(images, [batch_size, image_size, image_size, depth])
  labels = tf.reshape(labels, [batch_size, 1])
  indices = tf.reshape(tf.range(0, batch_size, 1), [batch_size, 1])
  labels = tf.sparse_to_dense(
      tf.concat(values=[indices, labels], axis=1),
      [batch_size, num_classes], 1.0, 0.0) 
  return images, labels
