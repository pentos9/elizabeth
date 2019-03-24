#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shutil_which.py
# @Author: lucas
# @Date  : 3/24/19
# @Desc  :


import shutil
import os
import logging
from shutil import copytree, ignore_patterns
from pprint import pprint


def _logpath(path, names):
    logging.info('working in %s' % path)
    return []


def copy_tree(src, dest, symlinks=False):
    names = os.listdir(src)
    os.makedirs(dest)

    for name in names:
        src_name = os.path.join(src, name)
        desc_name = os.path.join(dest, name)

        try:
            if symlinks and os.path.islink(src_name):
                link_to = os.readlink(src_name)
                os.symlink(link_to, desc_name)

            elif os.path.isdir(src_name):
                copy_tree(src_name, desc_name, symlinks)
        except OSError as why:
            pass
        except shutil.Error as err:
            pass


def copy_tree2(src, dest, ignore=ignore_patterns('*.pyc', 'tmp*')):
    shutil.copytree(src, dest, ignore)


def run():
    path = shutil.which("python")
    pprint(path)


if __name__ == '__main__':
    run()
