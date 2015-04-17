chrome_extensions_downloader
============================

It's a tool that can download chrome extensions to your pc and save as *.crx

## Requirements ##

* [Python 2.7](https://www.python.org/downloads/) (recommend)
* [requests](http://www.python-requests.org/en/latest/)
* Linux/Mac/Windows

## How to use ##

```python crx.py -u url [-p proxy]```<br />
<br />

## Sample ##

Now i want to download "adblock-plus"<br />
It's url is "https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb"<br />
It's id is "cfhdojbkjhnklbpkdaibdccddilifddb"<br />
I can download it like this<br />

```python crx.py -u https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb```<br />
Or<br />
```python crx.py -u cfhdojbkjhnklbpkdaibdccddilifddb```<br />
If i want to use a proxy, i use goagent, so my proxy is "127.0.0.1:8087", i can use it like this<br />
```python crx.py -u https://chrome.google.com/webstore/detail/adblock-plus/cfhdojbkjhnklbpkdaibdccddilifddb -p 127.0.0.1:8087```<br />
Or<br />
```python crx.py -u cfhdojbkjhnklbpkdaibdccddilifddb -p 127.0.0.1:8087```<br />

If you're in china, you should use a proxy
