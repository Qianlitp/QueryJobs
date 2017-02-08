#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 查询给定网站的招聘发布


import requests
import re


# 获取网页源码
def getHTML(url):
    r = requests.get(url)
    r.encoding = 'utf-8'    # requests 模块会根据响应头来推测编码，但又是无法正确找出编码，所以直接给定编码
    return r.text


# 根据所给关键词正则匹配
# 如果所给的关键词无法匹配 ，则说明网页产生了变化
def analyze(content, patt, name, flag):
    m = re.search(unicode(patt, "utf-8"), content)
    if m is not None and flag == 0:
        print name, ' no job.'
    elif m is None and flag == 1:
        print name, ' no job.'
    else:
        print name, ' is change!'


# 从配置文件中读取站点列表
def read_conf():
    site_list = []
    f = open('sites')
    for line in f:
        info = line.split(' ')
        # 六列分别对应 (公司、url、匹配方式、关键词)
        # 其中 0 代表匹配存在的内容，1 代表匹配希望出现的内容
        site_list.append((info[0], info[1], info[2], info[3][:-1]))
    return site_list


def main():
    sites = read_conf()
    for each in sites:
        content = getHTML(each[1])
        analyze(content, each[3], each[0], int(each[2]))

if __name__ == '__main__':
    main()
