#https://blog.shichao.io/2012/10/04/progress_speed_indicator_for_urlretrieve_in_python.html

import os, sys, time
import tarfile
import urllib

def reporthook(count, block_size, total_size):
  global start_time
  if count == 0:
    start_time = time.time()
    return
  duration = time.time() - start_time
  progress_size = int(count * block_size)
  percent = int(count * block_size * 100 / total_size)
  sys.stdout.write('\r...%d%%, %d MB, %d seconds passed' %
                   (percent, progress_size / (1024 * 1024), duration))
  sys.stdout.flush()

cifar10url = 'https://www.cs.toronto.edu/~kriz/cifar-10-binary.tar.gz'
cifar10 = '%s/cifar-10-binary.tar.gz' % os.environ['HOME']
cifar10_extracted = '%s/cifar-10-batches-bin' % os.environ['HOME']

def download():
  if not os.path.isfile(cifar10):
    urllib.urlretrieve(cifar10url, cifar10, reporthook)
  print()
  print('Download finished!')

  if not os.path.isdir(cifar10_extracted):
    tarfile.open(cifar10, 'r:gz').extractall(os.path.dirname(cifar10_extracted))
  print('Uncompression finished!')

