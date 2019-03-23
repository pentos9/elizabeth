#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : os_walk_file.py
# @Author: lucas
# @Date  : 3/22/19
# @Desc  :


import os
import zipfile
from pprint import pprint


def check_path(path=None):
    if not path:
        raise Exception("patn is Noe" % path)

    if not os.path.exists(path):
        raise Exception("path:%s not exist" % path)


def traverse(path=None, post_fix='.py'):
    check_path(path)
    for folder_name, sub_folders, file_names in os.walk(path):
        for file_name in file_names:
            if not file_name.endswith(post_fix):
                return
            pprint(file_name)


def zip_file(path=None, source_file=None, mode='w'):
    with zipfile.ZipFile(path, mode) as target_zip_file:
        target_zip_file.write(source_file, compress_type=zipfile.ZIP_DEFLATED)
        pprint(target_zip_file.namelist())


def unzip_file(path=None, dest_path=None):
    with zipfile.ZipFile(path, 'r') as target_zip_file:
        target_zip_file.extractall(dest_path)


def run():
    path = '/Users/lucas/projects/elizabeth'
    traverse(path)
    zip_file('/Users/lucas/projects/elizabeth/app/core/os_walk_file.zip',
             '/Users/lucas/projects/elizabeth/app/core/os_walk_file.py')

    unzip_file('/Users/lucas/projects/elizabeth/app/core/os_walk_file.zip',
               '/Users/lucas/projects/elizabeth/app/core/zip')


if __name__ == '__main__':
    run()
