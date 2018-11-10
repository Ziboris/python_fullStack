#coding=utf-8
#version:python3.6.0
#Tools:Pycharm 2017.3.2
__date__ = ' 2018/11/3 20:23'
__author__ = 'ziboris'

from django import template
from django.utils.safestring import mark_safe

register=template.Library() #register这个变量的名字是固定的，不可改变

# 装饰器
@register.filter
def filter_multi(x,y):
    #默认x是|之前的变量
    return x*y

@register.simple_tag
def test_simple_tag(x,y):
    return x*y
