#!/usr/bin/env python
# -*- coding:utf-8 -*-

#####################################
#
# author:chenmengting01@baidu.com
#
# 2017-06-08 10:34:14
#
#####################################
"""
function: accessing the online service,
parsing the JSON result, and returning
"""
import urllib2
import json
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')

class VideoHttp(object):
    """
    function: accessing the online service,
    parsing the JSON result, and returning
    """
    def getHtml(self, url):
        """
        function: accessing web services to get web results
        """
        headers = { 'Host':'baijiahao.baidu.com',
        'Connection':'keep-alive',
        'Cache-Control':'no-cache',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Referer': 'http://baijiahao.baidu.com/builder/article/list',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'
        }
        req = urllib2.Request(url, headers = headers)
        req.get_method=lambda: 'GET'
        #page = urllib2.urlopen(req)
        page = urllib2.urlopen(url)
        code = page.getcode()
        print "status code %s" % page.getcode()
	if code != 200:
            print "error code %s " % code
        html = page.read()
        return html

    def bd_dic(self, key, dic):
        """
        function: JSON parsing
        """
        if key in dic:
            return str(dic[key])
        else:
            return ''

    def bd_dic_dic(self, key, dic):
        """
        function: JSON parsing
        """
        if key in dic:
            return dic[key]
        else:
            return ''

    def get_feature(self, url):
        """
        function: implementation services
        """
        html = self.getHtml(url)
        self.write_file(url, html)
        return 0

    def write_file(self, url, html):
        file_object = open('tmp/' + '1', 'w')
        file_object.write(html)
        file_object.close()
        return 0


VH = VideoHttp()

def diff_list(url, lista, listb):
    """
    function: check the diff between lista and listb
    """
    lena = len(lista)
    lenb = len(listb)
    if lena != lenb:
        print "Error: not equal (%s)" % url
        return -1
    for i in range(lena):
        if lista[i] != listb[i]:
            return -1
    return 0

def run():
    url = 'http://cp01-online-learning2.epc.baidu.com:8600 \
        /VideoSrv/recommend?title=∏¯Œ“–°”„! \
        &BAIDUID=&charset=utf-8&forcesid=etoe'
    file_path = './data/url.txt'
    file_object = open(file_path)
    i = 0
    while 1:
        line = file_object.readline()
        if not line:
            break
        url = line
        HV = VideoHttp()
        i += 1
        print "NOTICE old %s i = %d" % (time.strftime('%H:%M:%S', time.localtime(time.time())), i)
        ret = HV.get_feature(url)
        print "NOTICE new %s i = %d" % (time.strftime('%H:%M:%S', time.localtime(time.time())), i)
        if ret != 0:
            print "Result Error: (%s) fail " % url
        else:
            print "Result Equal: (%s) ok" % url
        print "sleep 1s"
        time.sleep(2)
    file_object.close()

if __name__ == '__main__':
    i = 0
    print "NOTICE old %s i = %d" % (time.strftime('%H:%M:%S', time.localtime(time.time())), i)
    while i < 360000:
        print "run count = %d" % i
        run()
        i += 1
    print "run end!"
    print "NOTICE new %s i = %d" % (time.strftime('%H:%M:%S', time.localtime(time.time())), i)
