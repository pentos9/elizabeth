#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shutil_base.py
# @Author: lucas
# @Date  : 3/20/19
# @Desc  :


import shutil
import os

def copy(source_path=None, file_path=None, new_file_path=None):
    if not source_path:
        return
    os.chdir(source_path)
    shutil.copy(file_path, new_file_path)


def move():
    pass


def run():
    copy(source_path=u'/Users/lucas/projects/elizabeth', file_path=u'README.md', new_file_path='README-2.md')


if __name__ == '__main__':
    run()