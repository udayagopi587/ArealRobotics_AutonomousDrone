# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:50:42 2022

@author: udaya
"""

import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print(tf.__version__)