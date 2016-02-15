#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import os
import tarfile
import urllib
from IPython.display import display, Image
from scipy import ndimage
from sklearn.linear_model import LogisticRegression
import cPickle as pickle

print "Hello world\n"

url = 'http://yaroslavvb.com/upload/notMNIST/'

def maybe_download(filename, expected_bytes): #creates a function
  """Download a file if not present, and make sure it's the right size."""
  if not os.path.exists(filename): #if the file is not in the directory
    filename, _ = urllib.urlretrieve(url + filename, filename) #I don't know what's going on here.
    print filename
  statinfo = os.stat(filename)
  if statinfo.st_size == expected_bytes:
    print 'Found and verified', filename
  else:
    raise Exception(
      'Failed to verify' + filename + '. Can you get to it with a browser?')
  return filename

train_filename = maybe_download('otMNIST_large.tar.gz', 247336696)
test_filename = maybe_download('notMNIST_small.tar.gz', 8458043)
