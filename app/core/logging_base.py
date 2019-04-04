#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : logging_base.py
# @Author: lucas
# @Date  : 4/4/19
# @Desc  :

import os
import pprint
import logging

logging.basicConfig(filename='log.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def list_dir():
    for filename in os.listdir():
        if filename.endswith('.py'):
            pprint.pprint(filename)


def run():
    logger.info("list dir")
    list_dir()


if __name__ == '__main__':
    run()
