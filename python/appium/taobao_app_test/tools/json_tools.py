# -- coding: utf-8 -
"""
@project    :HandBook
@file       :json_tools.py
@Author     :wooght
@Date       :2024/9/17 1:13
@Content    :
"""
import json


def get_url_params(url):
    """
    获取get地址中的参数
    :param url:
    :return:
    """
    url_native = url.replace('\\', '')
    url_native = url_native.replace('"{', '{')
    url_native = url_native.replace('}"', '}')
    return json.loads(url_native)


def get_key_words(p):
    """
    返回参数列表, 多级按照:连接
    :param p:
    :return:
    """
    if isinstance(p, dict):
        key_words = []
        for key, value in p.items():
            if isinstance(value, dict):
                key_list = get_key_words(value)
                if isinstance(key_list, list):
                    for k in key_list:
                        key_words.append(key + ':' + k)
            else:
                key_words.append(key)
        return key_words
    else:
        return None


def get_multi_dict(p, l):
    """
    获取多级(不定级)dict的值
    """
    if len(l) > 1:
        c = p
        for k in l:
            c = c[k]
        return c
    else:
        return None


def get_params_diff(p1, p2):
    """
    参数对比,返回不同参数的key
    :param p1:
    :param p2:
    :return:
    """
    key_words = get_key_words(p1)
    key_words_p2 = get_key_words(p2)
    print('p1_key_words:', key_words, '\r\n p2_key_words:', key_words_p2)
    diff_key = {}
    for key in key_words:
        if key in key_words_p2:
            if ':' in key:
                p1_multi = get_multi_dict(p1, key.split(':'))
                p2_multi = get_multi_dict(p2, key.split(':'))
                if p1_multi != p2_multi:
                    diff_key[key] = f'p1:{key}:{p1_multi}, p2:{key}:{p2_multi}'
            else:
                if p1[key] != p2[key]:
                    diff_key[key] = f'p1:{key}:{p1[key]}, p2:{key}:{p2[key]}'
        else:
            if ':' in key:
                p1_multi = get_multi_dict(p1, key.split(':'))
                diff_key[key] = f'p1:{key}:{p1_multi}, p2:null'
            else:
                diff_key[key] = f'p1:{key}:{p1[key]}, p2:null'
    return diff_key
