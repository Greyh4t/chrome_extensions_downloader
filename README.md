chrome_extensions_downloader
============================

It's a tool that can download chrome extensions to your pc and save as *.crx

## Requirements ##

* [Python 2.7](https://www.python.org/downloads/) (recommend)
* Linux/Mac/Windows

## How to use ##

```python crx.py url [proxy]```<br />
Or<br />
```python crx.py id [proxy]```<br />
If you use windows and haven't python, You can use crx.exe in cmd like this<br />
```crx.exe url [proxy]```<br />
Or<br />
```crx.exe id [proxy]```<br />

## Sample ##

Now i want to download "proxy switchysharp"<br />
it's url is "https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm"<br />
it's id is "dpplabbmogkhghncfbfdeeokoefdjegm"<br />
i can download it like this<br />

```python crx.py https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm```<br />
Or<br />
```python crx.py dpplabbmogkhghncfbfdeeokoefdjegm```<br />
If i want to use a proxy, i use goagent, so my proxy is "127.0.0.1:8087", i can use it like this<br />
```python crx.py https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087```<br />
Or<br />
```python crx.py dpplabbmogkhghncfbfdeeokoefdjegm 127.0.0.1:8087```<br />

If you're in china, you should use a proxy  
