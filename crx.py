#coding:utf-8
import urllib, urllib2, sys, re, os

user_agent = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.3 Safari/537.36'
proxy = ''

path = sys.path[0]
if os.path.isfile(path):
    path = os.path.dirname(path)
if len(sys.argv) < 2:
    print """
    Please add a url parameters. if you're in china, please use proxy.

    sample:
    python crx.py https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087
    or:
    python crx.py dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087
    """
    print 'Press the Enter key to exit'
    raw_input()
    sys.exit()

if len(sys.argv) == 3:
    proxy = sys.argv[2]
target = sys.argv[1]

if 'chrome.google.com' in target:
    tmp = re.findall(r'detail/(.*?)/(\w+)', target)
    if not tmp:
        print """
    Please use a correct url or extension ID.

    sample:
    https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm
    or:
    dpplabbmogkhghncfbfdeeokoefdjegm
    """
        print 'Press the Enter key to exit'
        raw_input()
        sys.exit()
    crx_name = tmp[0][0]
    crx_id = tmp[0][1]
elif re.match('^[a-z]+$', target):
    crx_name = 'extension'
    crx_id = target
else:
    print """
    Please use a correct url or extension ID.

    sample:
    https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm
    or:
    dpplabbmogkhghncfbfdeeokoefdjegm
    """
    print 'Press the Enter key to exit'
    raw_input()
    sys.exit()

if '%' in crx_name:
    crx_name = urllib.unquote(crx_name)

download_url = 'https://clients2.google.com/service/update2/crx?response=redirect&x=id%3D' + crx_id + '%26uc'

if proxy:
    opener = urllib2.build_opener(urllib2.ProxyHandler({'https':proxy}))
else:
    opener = urllib2.build_opener(urllib2.ProxyHandler({}))
opener.addheaders = [('User-agent', user_agent)]

try:
    print 'Downloading...'
    get_crx = opener.open(download_url, timeout = 30)
    crx_version = re.findall(r'extension(\w*?.crx)', get_crx.geturl())[0]
    file = get_crx.read()
except Exception, e:
    print e
    print ''
    print 'Download failed'
    if not proxy:
        print 'Please try to use a proxy'
    print 'Press the Enter key to exit'
    raw_input()
    sys.exit()

crx = open(unicode(path + '/' + crx_name + crx_version, 'utf-8'), 'wb')
crx.write(file)
crx.close()
print 'Download success to ' + unicode(path + '/' + crx_name + crx_version, 'utf-8')
print 'Press the Enter key to exit'
raw_input()