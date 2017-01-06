#!/usr/bin/python3
# -*- coding: UTF-8 -*-


from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys, getopt


def login():
    url = 'https://w.seu.edu.cn/index.php/index/login'
    post_data = {'username':'your ID ','password':'password using base64','enablemacauth':0}
    # use https://www.base64encode.org/ using UTF-8 to convert password to base64 format.

    request = Request(url, urlencode(post_data).encode())
    json = urlopen(request).read().decode()
    #print(json)


def logout():
    url = 'https://w.seu.edu.cn/index.php/index/logout'
    request = Request(url, urlencode({}).encode())
    json = urlopen(request).read().decode()
    #print(json)


if __name__ == "__main__":
    # print(sys.argv)
    argvs = sys.argv
    if argvs[1]=='-i':
        login()
    elif argvs[1]=='-o':
        logout()
    else:
        print('Wrong')
