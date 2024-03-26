import os
import logging

if 'RMSN_VERSION' not in os.environ:
    logging.info("No env variable RMSN_VERSION found. Defaulting to v1.")
    os.environ['RMSN_VERSION'] = 'v1'

if "compat" == os.environ['RMSN_VERSION']:
    import tensorflow.compat.v1 as tf
    tf.disable_v2_behavior()
    from tensorflow.compat.v1.nn.rnn_cell import RNNCell, BasicLSTMCell
    from tensorflow.compat.v1.keras.initializers import glorot_normal as xavier_initializer
    from tensorflow_probability.stats import percentile
    from tensorflow.compat.v1.linalg import matmul
else:
    if "v1" != os.environ['RMSN_VERSION']:
        logging.info("Version RMSN_VERSION not valid. Defaulting to v1.")
    import tensorflow as tf
    from tensorflow.contrib.rnn import RNNCell, BasicLSTMCell
    from tensorflow.contrib.layers import xavier_initializer
    from tensorflow.contrib.distributions import percentile
    from tensorflow import matmul