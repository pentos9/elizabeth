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

    if not os.path.exists(source_path):
        return
    os.chdir(source_path)
    shutil.copy(file_path, new_file_path)


def move(source_path=None, dest_path=None):
    if not (source_path or dest_path):
        return

    if not os.path.exists(source_path):
        return

    parent_dir = os.path.dirname(dest_path)
    if not os.path.exists(parent_dir):
        print('parent:%s not exist' % parent_dir)
        return
    shutil.move(source_path, dest_path)


def run():
    source_path = u'/Users/lucas/projects/elizabeth'
    source_file_name = u'README.md'
    new_file_name = u'README-2.md'
    copy(source_path=source_path, file_path=source_file_name, new_file_path=new_file_name)
    move(source_path + '/' + new_file_name, source_path + '/app/' + new_file_name)


if __name__ == '__main__':
    run()
