#!/usr/bin/env python
# coding: utf-8

import hashlib
from debug import debug


def get_md5_value(value):
    """
    计算md5值
    """
    m = hashlib.md5()
    try:
        if value:
            m.update(value)
        md5digest = m.hexdigest()
        return md5digest
    except:
        traceback.print_exc()
    return None
