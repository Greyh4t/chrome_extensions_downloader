#coding:utf-8
import requests
import argparse
import re
import os


parser = argparse.ArgumentParser()
parser.add_argument('-u', help = u'''扩展的地址或者ID，类似
                                     https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb
                                     或
                                     cfhdojbkjhnklbpkdaibdccddilifddb''', required = True)
parser.add_argument('-p', help = u'''代理地址，类似
                                     127.0.0.1:8087''')
args = parser.parse_args()


def over():
    print 'Press the Enter key to exit'
    raw_input()


def download():
    target = args.u
    proxies = {'http': args.p,
            'https': args.p,
    }

    if 'chrome.google.com' in target:
        tmp = re.search(r'detail/(.*?)/(\w+)?', target)
        if tmp:
            crx_name = tmp.group(1)
            crx_id = tmp.group(2)
    elif re.match('^[a-z]+$', target):
        crx_name = 'extension'
        crx_id = target
    else:
        print u'请输入正确的链接或ID'
        return
        over()

    url = 'https://clients2.google.com/service/update2/crx?response=redirect&prodversion=43.0.2357.10&x=id%3D' + crx_id + '%26installsource%3Dondemand%26uc'
    print u'下载中，请稍后...'
    r = requests.get(url, proxies = proxies, verify=False)
    crx_version = re.search(r'extension(\w*?.crx)', r.url).group(1)

    path = os.path.split(os.path.realpath(__file__))[0]
    with open (path + os.sep + crx_name + crx_version, 'wb') as f:
        f.write(r.content)
        print u'下载成功'
    over()


download()
