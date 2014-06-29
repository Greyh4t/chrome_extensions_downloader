chrome_extensions_downloader
============================

It's a tool that can download chrome extensions to your pc and save as *.crx

## Requirements ##

* [Python 2.7](https://www.python.org/downloads/) (recommend)
* Linux/Mac/Windows

## How to use ##

python crx.py url [proxy]\
Or,
python crx.py id [proxy]\

If you use windows and haven't python, You can use crx.exe in cmd like this
    
crx.exe url [proxy]\
Or,
crx.exe id [proxy]\

## Sample ##

Now i want to download "proxy switchysharp", it's url is "https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm", it's id is "dpplabbmogkhghncfbfdeeokoefdjegm", i can download it like this

python crx.py https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm\
Or,
python crx.py dpplabbmogkhghncfbfdeeokoefdjegm\

If i want to use a proxy, i use goagent, so my proxy is "127.0.0.1:8087", i can use it like this

python crx.py https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087\
Or,
python crx.py dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087\

If you're in china, you should use a proxy  