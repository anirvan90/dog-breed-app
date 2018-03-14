from scipy.misc import imread, imresize, imshow
import numpy as np
import tensorflow as tf
import keras.models
import sys, os
sys.path.append(os.path.abspath('./model'))
from load import *
global model, graph

model, graph = init()

test_img = 
