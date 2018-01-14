from __future__ import print_function, absolute_import, division

import numpy as np
from .test_module import processImage as processImage2
from .test_module import setWeights

weights_npy='mlp_model.npz'

W, b = {}, {}
with np.load(weights_npy) as f:
    n_layers = len(f.files) // 2
    for i in range(len(f.files)):
        # print(f['arr_%d' % i].shape)
        if i % 2 == 1:
            b[i // 2] = f['arr_%d' % i].astype(np.float32)
        else:
            W[i // 2] = f['arr_%d' % i].astype(np.float32)

setWeights(W[0], b[0], W[1], b[1], W[2], b[2])