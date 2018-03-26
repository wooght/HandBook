# -*- coding: utf-8 -*-
#
# @method   : logging 应用
# @Time     : 2017/11/18
# @Author   : wooght
# @File     : base.py

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s:: %(message)s',
                    datefmt='%d-%H:%M:%S',
                    )


class lg:

    @staticmethod
    def e(charts):
        logging.info(charts)

    @staticmethod
    def error(charts):
        logging.warning(charts)


lg.e('echo')
