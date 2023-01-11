## About
基于 Python3 采集股票信息，并将数据保存到csv文件

## Feature

* 采集股票信息, 网站以 https://www.taifex.com.tw/cht/9/futuresQADetail 为例
* 引用 BeautifulSoup 库, 实现选择html DOM
* 存储数据为csv文件

## Requires
Python 3.11.0  
beautifulsoup4 4.11.1  
requests 2.28.1  
pandas 1.5.2  

## Usage
```
python main.py
```

## Change Log
v1.0.0  

v1.0.1 
* 使用select选择器, 选取规则简单直观

## Maintainers
Alan

## LICENSE
[MIT License](https://github.com/joanbabyfet/collect_stock/blob/master/LICENSE)