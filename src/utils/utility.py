import os
import random
import time
from collections import OrderedDict
from contextlib import contextmanager

import numpy as np
import torch


def fix_seed(seed=1119):
    '''
    fix seed as follows:
    - random
    - python hash seed
    - numpy
    - torch
    if you add lib,  please leave what lib you add
    '''

    random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True


@contextmanager
def timer(name: str) -> None:
    """Timer Util"""
    t0 = time.time()
    print("[{}] start".format(name))
    yield
    print("[{}] done in {:.0f} s".format(name, time.time() - t0))


def fix_model_state_dict(state_dict):
    new_state_dict = OrderedDict()
    for k, v in state_dict.items():
        name = k
        if name.startswith('model.'):
            name = name[6:]  # remove 'module.' of dataparallel
        new_state_dict[name] = v
    return new_state_dict


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def file_path(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)
